#클래스 선언 (속성)
class post:
    author = mame
    likes = 0
    content = "What are you doing?"


 #클래스 선언 (메소드)
 class Post :
    def like(self,user) :
        self.like += 1
        user.liked_posts.append(self)


#생성자 : 객체가 만들어질 때, 자동으로 호출되는 메서드
class Post :
    def __inin__ (self, author, content) :

# 클래스 내부의 속성/메소드에 접근할 때
class Post :

    def __init__(self, author, content):
        self.author = author
        self.content = content

my_post = Post('elice','I Love Coding!')

print(my_post.author)
print(my_post.content)

#속성을 만들 때 주의 할 점
#같은 내용을 나타내는 속성이 2개
## like와 like_count가 사실상 같은 정보를 나타냄
## 코드 작성자나 협업자가 헷갈릴 수 있으며
## 이후 값이 따로따로 변경되면 데이터 불일치 발생할 수 있음

class Post : 
    def __init__(self, author, content):
        self.like = 0
        self.liked_users = []


class Post : 
    def __init__(self, author, content):
        self.like = 0
        self.liked_users = []

my_post = Post('elice','I Love Coding!')
my_post.like+=1


#메소드 만들기
## 메소드를 속성처럼 사용
class Post : 
    def num_like(self) :
        return len(self.liked_users)
    


class Post:
    def __init__(self):
        self.liked_users = []
    def num_likes(self):
        return len(self.liked_users)
    
my_post = Post()
my_post.liked_users.append('elice')

print(my_post.num_likes())



#