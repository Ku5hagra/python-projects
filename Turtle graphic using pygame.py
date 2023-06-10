import turtle
window = turtle.Screen()
window.bgcolor('BLACK')
rob = turtle.Turtle()
rob.speed(500)
colors=["red","blue","navy","darkturquoise","mediumspringgreen","royalblue","chartreuse","olivedrab","plum","lightgreen","skyblue","brown","cyan","indigo","rosybrown","lightseagreen","palegreen","fuchsia","violet","tan","purple","darkcyan"]
for i in range(40,403):
   rob.color(colors[i%(len(colors))])
   rob.forward (i)
   rob. right(91)
