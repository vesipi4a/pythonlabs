tpl = ()
for i in range(0, 7):
    tpls = input("Vuvedete niz: ")
    tpl=tpl+(tpls,)

print(tpl)
print(max(tpl))
