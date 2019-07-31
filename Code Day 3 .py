print(cadbury1,cadbury2,cadbury3)
print("cadbury1","cadbury2","cadbury3")
print("milk chocolate","dark chocalte","white chocolate")
darkchocalte = 5
milk = 6
white =8

print(white)
choc1 = {"darkchocolate":5}
choc1 = {"darkchocolate":5}
choc2 = {"milkchocolate":6}
choc3 = {"whitechoolate":8}
chocolatebox ={"dark":5,"milk":6,"white":8}
name = {"steve":32,"lia":28,"vin":45,"katie":38}
studentgender = {"steve":"M","lia":"F","vin":"M","katie":"F"}
studentgender
studentlis = [[]]
studentlist= [['steve',32,'m'],["lia",28,"f"],["vin",45,"m"],["katie",38,"f"]]
studentlist
student = [name,studentgender]
student
import pandas
dir(pandas)
studentdf = pandas.DataFrame(studentlist)
studentdf
studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf
studentdf["name"]

studentgender = {"steve":"M","lia":"F","vin":"M","katie":"F"}
studentgender
studentdf["studentgender"]
studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf
studentdf["name"]
studentdf["studentgender"]
studentdf["gender"]
chocolates = [["milk",5],["dark",6],["white",8]]
chocodf = pandaDataFrame(chocolates,columns=("chocolate","quantity")
