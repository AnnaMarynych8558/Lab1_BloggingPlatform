from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from models import User, Post, Comment, Category
from forms import LoginForm, RegistrationForm, PostForm, CommentForm, CategoryForm

@app.route('/')
@app.route('/index')
def index():
    """Homepage showing all blog posts"""
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category', type=int)
    
    # Base query
    posts_query = Post.query.order_by(Post.created_at.desc())
    
    # Filter by category if specified
    if category_id:
        posts_query = posts_query.filter_by(category_id=category_id)
    
    # Paginate results
    posts = posts_query.paginate(
        page=page, per_page=10, error_out=False
    )
    
    categories = Category.query.all()
    selected_category = Category.query.get(category_id) if category_id else None
    
    return render_template('index.html', posts=posts, categories=categories, 
                         selected_category=selected_category)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new blog post"""
    form = PostForm()
    if form.validate_on_submit():
        category_id = form.category_id.data if form.category_id.data != 0 else None
        post = Post(
            title=form.title.data,
            summary=form.summary.data,
            content=form.content.data,
            user_id=current_user.id,
            category_id=category_id
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been published!', 'success')
        return redirect(url_for('post_detail', id=post.id))
    
    return render_template('create_post.html', form=form)

@app.route('/post/<int:id>')
def post_detail(id):
    """Show individual post with comments"""
    post = Post.query.get_or_404(id)
    comments = Comment.query.filter_by(post_id=id).order_by(Comment.created_at.asc()).all()
    form = CommentForm() if current_user.is_authenticated else None
    
    return render_template('post_detail.html', post=post, comments=comments, form=form)

@app.route('/post/<int:id>/comment', methods=['POST'])
@login_required
def add_comment(id):
    """Add a comment to a post"""
    post = Post.query.get_or_404(id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            post_id=post.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Comment error: {error}', 'danger')
    
    return redirect(url_for('post_detail', id=id))

@app.route('/post/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    """Edit an existing post"""
    post = Post.query.get_or_404(id)
    
    # Check if current user is the author
    if post.user_id != current_user.id:
        abort(403)
    
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.summary = form.summary.data
        post.content = form.content.data
        post.category_id = form.category_id.data if form.category_id.data != 0 else None
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post_detail', id=post.id))
    
    return render_template('edit_post.html', form=form, post=post)

@app.route('/post/<int:id>/delete', methods=['POST'])
@login_required
def delete_post(id):
    """Delete a post"""
    post = Post.query.get_or_404(id)
    
    # Check if current user is the author
    if post.user_id != current_user.id:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(user_id=current_user.id).order_by(
        Post.created_at.desc()
    ).paginate(page=page, per_page=10, error_out=False)
    
    return render_template('profile.html', posts=posts)

@app.route('/create_category', methods=['GET', 'POST'])
@login_required
def create_category():
    """Create a new category (admin function)"""
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(category)
        db.session.commit()
        flash('Category created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_category.html', form=form)

@app.errorhandler(403)
def forbidden(error):
    return render_template('error.html', 
                         error_code=403, 
                         error_message="You don't have permission to access this resource."), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', 
                         error_code=404, 
                         error_message="The page you're looking for doesn't exist."), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', 
                         error_code=500, 
                         error_message="An internal server error occurred."), 500
