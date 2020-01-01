from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
	"""this function is used to send a request to server for registeration"""
	data = request.POST.dict()	
	l = []
	for i in User.objects.all():
		l.append(i.username)
	if(data['username'] in l):
		return HttpResponse('you cant register!')
	else:
		person = User.objects.create(name=data['name'], familyname=data['familyname'], username=data['username'], password=data['password'], gender=data['gender'])
		request.session['User_id'] = person.id
		request.session.save() 
		return HttpResponse('you haved register!')

@csrf_exempt
def login(request):
	"""this function is used to send a request to server for login"""
	data = request.POST.dict()
	l = []
	p = []
	for i in User.objects.all():
		l.append(i.username)
		p.append(i.password)
	t = dict(zip(l, p))
	if(data['username'] in l):
		if(t[data['username']]==data['password'] ):
			for i in User.objects.all():
				if(i.username==data['username']):
					request.session['User_id'] = i.id
					request.session.save()
			return HttpResponse('you haved logged in', status=200)
		else:
			return HttpResponse('incorrect password')
	else:
		return HttpResponse('invalid username')

@csrf_exempt	
def logout(request):
	"""this function is used to send a request to server for logout"""
	if request.session.has_key('User_id'):
		del request.session['User_id']
		return HttpResponse('you have been logged out',status=200)
	else:
		return HttpResponse('you are not logged in')

q2players = []
q4players = []

@csrf_exempt
def gameq2clone(request):	
		ID = request.session['User_id']
		if(ID not in q2players):
			q2players.append(ID)
		while(len(q2players)<2):
			return HttpResponse('please wait')
		else:
			return HttpResponse('play game')			
	
@csrf_exempt
def gameq4clone(request):
		ID = request.session['User_id']
		if(ID not in q4players):
			q4players.append(ID)
		while(len(q4players)<4):
			return HttpResponse('please wait')
		else:		
			return HttpResponse('play game')


@csrf_exempt
class gameq2 :
        board_player = [[ '-' for i in range(9)] for j in range(9)]
        board_hwall = [['-' for i in range(9)] for j in range(9)]
        board_vwall = [['-' for i in range(9)]for j in range(9)]
        board_point = [['-' for i in range(8)]for j in range(8)]
        board_player[8][4] = '*'
        board_player[0][4] = '+'
        player1w = 0
        player2w = 0
        @csrf_exempt
        def turn(request): 
                return HttpResponse('True')

        @csrf_exempt
        def is_end(request):
                for i in range(9):
                        if (gameq2.board_player[8][i]=='+' ):
                                return HttpResponse('True')                
                return HttpResponse('False')

        @csrf_exempt 
        def isvalidplayer(request):
                data = request.POST.dict()
                i = int(data['j'])
                j = int(data['i'])
                u = int(data['k'])
                k = int(data['u'])
                
                if(gameq2.board_player[i][j] == '-'):
                      print('mohi')
                      if((u-i==1) and (k==j) and gameq2.board_hwall[i][j]=='-'):
                                gameq2.board_player[i][j] = '+'#character1
                                gameq2.board_player[u][k] = '-'
                                print(gameq2.board_player)
                                return HttpResponse('True')
                      elif((i-u==1)and(k==j) and gameq2.board_hwall[u][k]=='-'):
                                gameq2.board_player[i][j] = '+'#character1
                                gameq2.board_player[u][k] = '-'
                                print(gameq2.board_player)
                                return HttpResponse('True')
                      elif((j-k==1)and(i==u)and gameq2.board_vwall[u][k]=='-'):
                                gameq2.board_player[i][j] = '+'#character1
                                gameq2.board_player[u][k] = '-'
                                return HttpResponse('True')
                      elif((k-j==1)and(i==u)and gameq2.board_vwall[i][j]=='-'):
                                gameq2.board_player[i][j] = '+'#character1
                                gameq2.board_player[u][k] = '-'
                                return HttpResponse('True')
        @csrf_exempt 
        def isvalidvwall(request):#amodi
                data=request.POST.dict()
                j = int(data['i'])-1
                i = int(data['j'])
                if(i-1 in range(9) and gameq2.board_vwall[i][j]=='-' and gameq2.board_vwall[i-1][j]=='-'):
                        if(gameq2.board_point[i-1][j]=='-'):
                                gameq2.board_vwall[i][j] = '+'
                                gameq2.board_vwall[i-1][j] =  '+'
                                gameq2.board_point[i-1][j] = '.'
                                return HttpResponse('True')
                        return HttpResponse('False')
                return HttpResponse('False')
        @csrf_exempt  
        def isvalidhwall(request):#ofoghi
                data=request.POST.dict()
                j = int(data['i'])
                i = int(data['j'])-1
                if(j+1 in range(9) and gameq2.board_hwall[i][j]=='-' and gameq2.board_hwall[i][j+1]=='-'):
                        if(gameq2.board_point[i][j]=='-'):
                                gameq2.board_hwall[i][j] = '+'
                                gameq2.board_hwall[i][j+1] = '+'
                                gameq2.board_point[i][j] = '.'
                                return HttpResponse('True')
                        return HttpResponse('False')
        @csrf_exempt
        def havewall(request):
                if(gameq4.player1w<10):
                        return HttpResponse('True')
                else:
                        return HttpResponse('False')
        @csrf_exempt 
        def pluswall(request):
                gameq4.player1w = game.player1+1 
class gameq4 :
        board_player = [[ '-' for i in range(9)] for j in range(9)]
        board_hwall = [['-' for i in range(9)] for j in range(9)]#ofoghi j+1
        board_vwall = [['-' for i in range(9)]for j in range(9)]#amodi i-1 
        board_point = [['-' for i in range(8)]for j in range(8)]
        board_player[8][4] = '*'
        board_player[0][4] = '+'
        board_player[4][0] = '&'
        board_player[4][8] = '#'
        turn = 0
        player1w = 0
        player2w = 0
        player3w = 0
        player4w = 0
        def is_end(self):
                for i in range(9):
                        if (self.board_player[8][i]=='+' or self.board_player[0][i]=='*' or self.board_player[i][0]=='#' or self.board_player[i][8]=='&'):
                                if(self.turn==0):
                                        print('player1 you win')
                                elif(self.turn==1):
                                        print('player2 you win')
                                elif(self.turn==2):
                                        print('player3 you win')
                                else:
                                        print('player4 you win')
                                return True
                return False
        def isvalidplayer(self,i,j,u,k):
                i, j = j, i
                u, k = k, u
                if(self.turn==0):
                        character1 = '+'
                        character2 = ['*', '&', '#']
                elif(self.turn==1):
                        character1 = '*'
                        character2 = ['+', '&', '#']
                elif(self.turn==2):
                        character1 = '&'
                        character2 = ['+', '*', '#']
                else:
                        character1 = '#'
                        character2 = ['+', '&', '*']
                if(self.board_player[i][j] == '-'):
                      if((u-i==1) and (k==j) and self.board_hwall[i][j]=='-') :
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((i-u==1)and(k==j) and self.board_hwall[u][k]=='-'):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(i==u)and self.board_vwall[u][k]=='-'):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(i==u)and self.board_vwall[i][j]=='-'):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(i-u==1)and self.board_hwall[u][k]=='+' and 
                        self.board_hwall[u][k-1]=='+' and (self.board_player[u][k+1]==character2[0] or
                        self.board_player[u][k+1]==character2[1] or self.board_player[u][k+1]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(i-u==1)and self.board_hwall[u][k]=='+' and 
                           self.board_hwall[u][k+1]=='+'and (self.board_player[u][k-1]==character2[0] or
                           self.board_player[u][k-1]==character2[1] or self.board_player[u][k-1]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(u-i==1)and self.board_hwall[u-1][k]=='+'and
                          self.board_hwall[u-1][k-1]=='+' and (self.board_player[u][k+1]==character2[0] or
                          self.board_player[u][k+1]==character2[1] or self.board_player[u][k+1]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(u-i==1)and self.board_hwall[u-1][k]=='+'and 
                          self.board_hwall[u-1][k+1]=='+' and (self.board_player[u][k-1]==character2[0] or
                          self.board_player[u][k-1]==character2[1] or self.board_player[u][k-1]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((u-i==2)and(j==k)and (self.board_player[u-1][j]==character2[0] or 
                           self.board_player[u-1][j]==character2[1] or self.board_player[u-1][j]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((i-u==2)and (j==k) and (self.board_player[u+1][j]==character2[0] or
                            self.board_player[u+1][j]==character2[1] or self.board_player[u+1][j]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==2)and(i==u) and (self.board_player[u][k+1]==character2[0] or
                           self.board_player[u][k+1]==character2[1] or self.board_player[u][k+1]==character2[2] )):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==2)and(i==u) and (self.board_player[u][k-1]==character2[0] or
                           self.board_player[u][k-1]==character2[1] or self.board_player[u][k-1]==character2[2])):
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      return False
                return False
        def isvalidvwall(self,i,j):#amodi
                i,j = j,i-1
                if(i-1 in range(9) and self.board_vwall[i][j]=='-' and self.board_vwall[i-1][j]=='-'):
                        if(self.board_point[i-1][j]=='-'):
                                self.board_vwall[i][j] = '+'
                                self.board_vwall[i-1][j] = '+'
                                self.board_point[i-1][j] = '.'
                                return True
                        return False
                return False
        def isvalidhwall(self,i,j):
                i,j=j-1,i
                if(j+1 in range(9) and self.board_hwall[i][j]=='-' and self.board_hwall[i][j+1]=='-'):
                        if(self.board_point[i][j]=='-'):
                                self.board_hwall[i][j] = '+'
                                self.board_hwall[i][j+1] = '+'
                                self.board_point[i][j] = '.'
                                return True
                        return False
                return False
        def have_wall(self):
                if(self.turn==0):
                        if(self.player1w<4):
                                return True
                        return False
                elif(self.turn==1):
                        if(self.player2w<4):
                                return True
                        return False 
                elif(self.turn==2):
                        if(self.player3w<4):
                                return True
                        return False   
                elif(self.turn==3):
                        if(self.player4w<4):
                                return True
                        return False
