agenda = {}
agenda["Carlos"] = "3001234567"
agenda["María"] = "3119876543"
agenda["Luis"] = "3205558899"

print("Agenda inicial:", agenda)
print("Número de María:", agenda.get("María"))

agenda["Luis"] = "3009991122"

print("Número de Luis actualizado:", agenda["Luis"])
del agenda["Carlos"]
print("Agenda final:", agenda)
