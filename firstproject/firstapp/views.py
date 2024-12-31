from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def display(request):
    ss='''
         <h2>hello html</h2>
         <hr/>
         '''
    return HttpResponse(ss) 
    
def show(request):
    ss='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>nav bar</title>
    <style>
        body{
            margin: 0px;
            padding: 0px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.7em;
        }
        a{
            text-decoration: none;
            color: #fff;
        }
        ul{
            list-style: none;
        }
        #nav{
            background-color: #333;
        }
        #sec{
            text-align: center;
            overflow: auto;
            /* margin: auto; */
            max-width: 1300px;
            /* padding: 0px 0px; */
        }
        #ul1{
            float: left;
            /* display: inline; */
        }
        #ul2{
            float: right;
        }
        #ul2 li{
            float: left;
            padding: 20px;
        }
        #ul1 a{
            display:block;
        }
        a:hover{
            background-color: #fff;
            color: #333;
        }
    </style>
</head>
<body>
    <nav id="nav">
        <div id="sec">
            <ul id="ul1">
                <li><h2><a href="#">HBT</a></h2></li>
            </ul>
            <ul id="ul2">
                <li><a href="#">home</a></li>
                <li><a href="#">about</a></li>
                <li><a href="#">contact</a></li>
            </ul>
        </div>
    </nav>
</body>
</html>
'''
    return HttpResponse(ss)

def hi(request):
    ss='''
    <html>
	<head>
		<title>***Welcome-Page***</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color="brown" width="45%"/>
		</center>
	</body>
</html>
'''
    return HttpResponse(ss)
def gitview(req):
    return HttpResponse("<h1>Hello From Git-View</h1><hr/>");    

