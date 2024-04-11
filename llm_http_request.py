import requests
import json
 
url = "https://prod.api.nvidia.com:443/llm/v1/azure/chat/completions"
 
payload = json.dumps({
   "model": "gpt-4",
   "messages": [
 	{
   	"role": "user",
   	"content": "Give me a 5 word answer on who is Sachin Tendulkar?"
 	}
   ],
   "temperature": 1,
   "top_p": 1,
   "n": 1,
   "stream": False,
   "max_tokens": 1000,
   "presence_penalty": 0,
   "frequency_penalty": 0
 })
 headers = {
   'correlationId': '8d2f9138-afde-4aae-8899-53ff4bdd6e8b',
   'Content-Type': 'application/json',
   'Authorization': 'Bearer eyJraWQiOiI3MjAzZGFhMC1mNDc3LTQ1MjAtYjQ2ZC1lYTY5NjdiZTYyYmUiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJudnNzYS1wcmQtRkVvVVlSb2dWZ1gtNTBtczdnMXhkczZiTFdObTRJYjh6RXVaLTZlZlRHMCIsImF1ZCI6WyJudnNzYS1wcmQtRkVvVVlSb2dWZ1gtNTBtczdnMXhkczZiTFdObTRJYjh6RXVaLTZlZlRHMCIsInM6NWtiZnhnYXFjM3hnejhuaGlkMXgxcjhjZmVzdG95cG4tdHJvZnV1bS1vYyJdLCJhenAiOiJudnNzYS1wcmQtRkVvVVlSb2dWZ1gtNTBtczdnMXhkczZiTFdObTRJYjh6RXVaLTZlZlRHMCIsInNlcnZpY2UiOnsibmFtZSI6IkVudGVycHJpc2UgSW50ZWdyYXRpb24gQXBwbGljYXRpb24iLCJpZCI6IjVrYmZ4Z2FxYzN4Z3o4bmhpZDF4MXI4Y2Zlc3RveXBuLXRyb2Z1dW0tb2MifSwiaXNzIjoiaHR0cHM6Ly81a2JmeGdhcWMzeGd6OG5oaWQxeDFyOGNmZXN0b3lwbi10cm9mdXVtLW9jLnNzYS5udmlkaWEuY29tIiwic2NvcGVzIjpbIm5lbW9sbG0tcmVhZHdyaXRlIiwiYXp1cmVvcGVuYWktcmVhZHdyaXRlIl0sImV4cCI6MTcxMjYyMDQyMCwidG9rZW5fdHlwZSI6InNlcnZpY2VfYWNjb3VudCIsImlhdCI6MTcxMjYxNjgyMCwianRpIjoiYzJlYjMxNjAtMGQyZi00OTc1LTk0NjktNTI4NzIyMjM3YjdlIn0.vXHZAfFt2MP_naF1XMwM85urvB1h_O5G4Wnma94v86ZeibUl6d4DfwX0qmHNgIs8cAxpUzZt22LDusAxDMymYQ'
 }
 
response = requests.request("POST", url, headers=headers, data=payload)

if response is None:
    print("Output Not Printed")
print(response.text)
