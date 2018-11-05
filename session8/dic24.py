# bảng lương 
salary = [
    {"Name" : "Huy" ,
    "Role" : "Waiter" ,
    "Hours" : 12 ,
    "Salary per Hour($)" : 0.8,
    },

    {"Name" : "Tung" ,
    "Role" : "Cook" ,
    "Hours" : 12 ,
    "Salary per Hour($)" : 1.5 ,
    },

    {"Name" : "M.Duc" ,
    "Role" : "Manager" ,
    "Hours" : 20 ,
    "Salary per Hour($)" : 2 ,
    },

    {"Name" : "Don" ,
    "Role" : "Waiter" ,
    "Hours" : 12 ,
    "Salary per Hour($)" : 0.8 ,
    },

    {"Name" : "H.Duc" ,
    "Role" : "Waiter" ,
    "Hours" : 14 , 
    "Salary per Hour($)" : 0.7 ,
    }
]

tol_sal = 0
for i in salary : 
    sal = round ( i["Hours"] * i["Salary per Hour($)"] ) * 30
    tol_sal += sal
print("The total money company must pay is", tol_sal, "dollars")