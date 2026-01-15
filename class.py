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


# 상속이 필요한 이유
# 여러 클래스가 비슷한 속성과 메소드를 공유해야 할 때
# 서로 다른 클래스 간의 계층 구조가 확실할 때


# (일반) 게시글

class Post :
    def __init__ (self, content):
        self.content = content



# 이미지가 있는 게시글

class ImagePost : 
    def __init__ (self, content, images) :
        self.content = content
        self.images = images

    def num-images(self) :
        return len(self,images)



# 클래스 상속
## 부모(부모의 속성, 메소드), 자식(부모의 속성, 메소드+ 자식의 속성, 메소드)

class Post : 
    def __init__ (self, content) :
        self.content = content


class ImagePost (Post) :
    def __init__ (self, content, images) :
        super().__init__(content)
        self.images = images


class Post :
    def __init__ (self, content) :
        self.content = content

class ImagePost (Post) : 
    def __init__ (self, content, images) :
        super().__init__(content)
        self.images = images

image_post = ImagePost(
    'Let's Coding!!!', 'home/elice/image.png'
)

print(image_post.content)
print(image_post.images)


#속성 상속
## 자식 클래스가 부모 클래스에 정의한 인스턴스 변수(속성)를 물려받아 사용할 수 있는 것
class Post : 
    def __init__ (self, content) :
        self.content = Content
        self.likers = []


## imagePost는 Post를 상속 받고 있음
## imagePost 객체를 생성할 때, 부모 생성자가 호출됨
### > 부모 클래스에서 정의할 self.cintent, self.likers가 my_post에 생성됨
class ImagePost(Post) :
    def __init__(self, content, images):
        super().__init__(content)
        self.images = images

my_post = ImagepOST(
    'elice 근처 맛집!!',
    'home/elice/image.png'
)

print(my_post.likers)


#속성 상속
## imagePost 안네 __init__ 생성자를 따로 정의하지 않았기 때문에, 자동으로 부모 클래스의 __init__ 이 호출
## my_post 를 만들 때, content 속성을 생성하고 likers 속성도 빈 리스트로 초기화

class Post : 
    def __init__ (self, content) :
        self.content = content
        self.likers = []

class ImagePost(Post) :
    pass
    
my_post = ImagePost('elice 근처 맛집!!')

print(my_post.likers)


## 자식 클래스에 __init__을 새로 정의하고 super()를 호출하지 않으면, 부모 속성은 초기화되지 않음
## 자식 클래스에서 부모 속성을 쓰고 싶다면 super().__init__()로 부모 생성자를 호출해야 함

class Post :
    def __init__ (self, content) :
        self.content = content
        self.likers = []

class ImagePost(Post) :
    def __init__(self, content, immages) :
        self.images = images

my_post = ImagePost(
    'elice 근처 맛집!!',
    'home/elice/image.png'
)

print(my_post.likers)


#메소드 상속
## 자식 클래스가 부모 클래스에서 정의된 메서드를 별도로 다시 작성하지 않고도 사용할 수 있게 하는 기능

class Post : 
    def __init__ (self. content)
        self.content = content
        self.likers = []

    def like (self, user) :
        self.likers.appenf(user)


## imagePost는 Post를 상속받고 있음
## imagePost에는 like() 메소드가 정의되어 있지 않음
## Post에서 정의된 like() 메소드를 자동으로 물려받음
## 자식 클래스는 부모의 기능을 그대로 사용함으로써 코드 중복을 줄이고 유지보수를 쉽게 만듦

class ImagePost(Post) :
    def __init__(self, content, images) :
        super().__init__(content)
        self.images = images

my_post = ImagePost(
    'elice 근처 맛집!!',
    'home/elice/image.png'
)

my_post.like('Bob')

print(my_post.likers)

#좋아요. 슬퍼요
class Like : 
    def __init__ (self, post, user) :
        self.post = post
        self.user = user

class Sad :
    def __init__ (self, post, user) :
        self.post = post
        self.user = user


#추상적인 부모 클래스
## 코드 중복 제거 : 자식 클래스마다 post,user 속성을 따로 작성하지 않아도 됨
## 구조 통일 : 모든 자식 클래스는 type, post, user을 가짐
## 확장 용이 : 새로운 반응(e.g.Angry등)을 추가할 때 부모 로직 재사용 가능
# 유지보수 편리 : 공통 로직을 한 곳(부모)에만 수정하면 됨

class Reaction : 
    def __init__ (self, _type, post, user)
        self.type = _type
        self. post = post
        self.user = user

#좋아요
class Like (reaction) :
    def __init__ (self, post, user)
        super().__init__('LIKE', post, user)

#싫어요
class Sad (Reaction) :
    def __init__ (self, post, user) :
        super().__init__('SAD', post, user)


# 이렇게 쓰진 않는다.
# 추상적인 부모 클래스는 직접 인스턴스화하지 않음
reaction = Reaction('vsadjkl', post, me)

#반드시 구체적인 자식 클래스로 쓴다.
like = Like(post, me)


#오버라이딩

class Post : 
    def __init__(self, content) : 
        self.content = content
        self.comments = {}

    def comment (self, user, comment) :
        self.comments[user] = comment

normal_post = Post('오공완(오늘도 공부 완료)!!!')

normal_post.comment('Sam', '너무 멋지다!!')
normal_post.comment('Queen', '나도 질 수 없지')

print(normal_post.comments)


# Post 클래스에는 원래 댓글을 저장하는 comment() 메서드가 존재
# ProtectedPost는 comment()를 오버라이딩(덮어쓰기)해서 댓글을 저장하지 않고 안내 메시지를 출력하도록 동작을 변경
# 같은 메서드 이름이지만 객체의 종류에 따라 결과가 달라짐

class ProtectedPost (Post) : 
    def comment (self, user, content) :
        print('who can reply? People the author mentioned can reply')

protected_post = ProtectedPost('보호된 게시물')

protected_post.comment('jojo','OH!! NO!!')

print(portected_post.comment)


# 모듈 불러오기
import string

print(string.digits)

from string import digits

print(string)


# 모든 코드는 모듈이다.
# 모듈이란 : 다른 코드에서 사용할 수 있도록 열어 놓은 코드
#posts.py
class Post :

class ImagePost(Post) :

#timeline.py
from posts import Post, ImagePost

timeline.add(Post('hello!'))
timeline.add(ImagePost('#food', []))

#패키지란? 모듈을 모아 놓은 폴더
#SNS / posts.py / users.py / media.py / ads.py

#패키지 안의 모듈
import SNS.users
from SNS import media
from SNS.posts import Post, ImagePost


#matplotlib
import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [3,5,8,2,5]

plt.bar(x, y, align='center')
plt.show()


#bar
import matplotlib.pyplot as plt

plt.bar(위치, 높이)
plt.show()

import matplotlib.pyplot as plt

x = range(5)
y = [5,4,3,2,1]

plt.bar(x, y)
plt.show()


#xticks() : x축 눈금 위치와 라벨(표시되는 값)을 설정하는 함수
import matplotlib.pyplot as plt

pos = range(4)
years = [2015, 2016, 2017, 2018]
temp = [17, 16, 19, 22]

plt.bar(pos, temp)
plt.xticks(pos, years)

#
import metplotlib.pylot as plt

pos = range(4)
years = [2015, 2016, 2017, 2018]
temp = [17, 16, 19, 22]

plt.par(pos, temp)


#
import metplotlib.pylot as plt

pos = range(4)
years = [2015, 2016, 2017, 2018]
temp = [17, 16, 19, 22]

plt.par(pos, temp)
plt.xticks(pos, years)