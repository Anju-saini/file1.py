# A login form also user can post  and access its thoughts and
class Account:
    # for structure and user input
    def __init__(self,username,password,name,phone_number):
        self.user_name = username
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.posts= []
        self.log_in = False
    #for log in
    def login(self,username,password):
        if username==self.user_name:
            if password==password:
                print("login")
                self.log_in=True
            else:
                print("invalid password")
        else:
            print("invalid username")
    # for post
    def post(self,p):
        if self.log_in == True:
          self.posts.append(p)
          print(p,"[posted]")
        else:
            print("plee login to post")
    # to see the post on my_wall
    def my_wall(self):
        print("\n posts")
        if self.log_in:
            i=1
            for post in self.posts:
              print(i,post)
              i += 1
        else:
            print("ples log in to show the post")
    # to chack the content if user login
    def get_info (self):
        if self.log_in == True:
            print("name={},phone_number ={}".format(self.name,self.phone_number))
        else:
            print("plese login")
    # for log out
    def logout(self):
        if self.log_in ==False:
            print("you are already log out")
        else:
            self.login=False
            print("logout")
#for output
user1 = Account(username="user1",password="pass1",name="ashi",phone_number=1234)
user2= Account(username="user2",password="pass2",name="anju",phone_number=12345)
user1.login(username="user1",password="pass1")
user1.get_info()
user1.post("hy how are you")
user1.post("happy")
user1.my_wall()
user1.logout()
user2.login(username="user2",password="pass2")
user2.get_info()
user2.logout()

