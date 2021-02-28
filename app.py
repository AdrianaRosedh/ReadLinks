from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class LinkPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ' Post ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_url = request.form['url']
        new_post = LinkPost(title=post_title, url=post_url)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = LinkPost.query.order_by(LinkPost.id).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = LinkPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    post = LinkPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.url = request.form['url']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():    
    if request.method == 'POST':
        post.title = request.form['title']
        post.url = request.form['url']  
        
        new_post = LinkPost(title=post_title, url=post_url)
        
        db.session.add(new_post)
        db.session.commit()
        
        return redirect('/posts')
    
    else:
        return render_template('new_post.html')


if __name__ == "__main__":
   # app.run(debug=True)
   db.create_all()
   app.run()