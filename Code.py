#Program To Calculate Bill For The Shop. Press The 'q' when you are done with your items. 
sum=0
print("***** Welcome To Our Shop!! *****")
while(True):
    num = input("Enter The Number:\n")
    if(num!="q"):
        sum=int(num)+sum
        print(f'Order Total so far: {sum}')
    else:
        print("You Have Pressed The Quit Button")
        break
print("The sum is",sum)
print('''***** Thanks for Shopping with us!! *****''')
