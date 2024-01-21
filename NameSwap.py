name = input("Enter full name:")
fn = name[:name.index(" ")]
sn = name[name.index(" ")+1:len(name)]
print(sn + " " + fn)