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



#원하지 않은 값 배제하기
class Post :
    def __init__(self):
        self,liked_user = []
     def num_likes(self):
        return len(self.liked_users)
    
my_post = Post('elice', 1457)
my_post.like(['Hello', 'World']')
             


#원하지 않은 값 배제하기(1)
# year_of_birth의 데이터 타입을 검사
## 숫자(int)가 아니라면 return 명령어 실행 -> 초기화 중단
class User:
    def __init__ (self, year_of_birth):
        if type(year_of_birth) is not int :
            return
        self.year_of_birth = year_of_birth

user1 = User(1994)
user2 = User('1994')

print(user1.year_of_birth)
print(user2.year_of_birth)



#원하지 않는 값 배제하기(2)
class User :
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, author, content):
        if not isinstance(author, User):
            return
        if type(content) is not str:
            return


author = User('elice')
my_post = Post.author('I Love Coding!')

print(my_post.author.name)
print(my_post.content)


your_post = Post('hellobit','Hello World!')

print(your_post.author.name)
print(your_post.content)


#[ref]isinstance??
## 객체의 자료형(타입)을 검사할 때 사용하는 python 내장 함수
### 첫번째 인자(객체) : 검사할 객체
### 두번째 인자(클래스 or 타입) : 확인할 클래스 또는 타입
### 반환값 : True or False
# isinstance(객체, 클래스 or 타입)
print(isinstance(5,int))
print(isinstance('hello', str))
print(isinstance(3.14, int))


class User :
    def __init__ (self, year_of_birth) :
        if year_of_birth > 2005 :
            raise Exception('Too young')

user1 = User(2000)
user2 = User(2006)


