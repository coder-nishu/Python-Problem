#8.There is a grocery shop which takes regular input from customers. After taking items if they want to add or remove items from their bucket list. We have to generate a program in python.
grocery = {
    "customer1" :  ["apple","banana","date"],
    "customer2" :  ["kola","lau","kodu"],
}
while true:
    n = int(input("Choose 1-5:"))
    match n:
        case 1: 
            grocery["customer1"].extend([item])

    
    