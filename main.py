
from prsaw import RandomStuffV2


rs = RandomStuffV2()


response = rs.get_ai_response("What is my name?")
print(response)


rs.close()