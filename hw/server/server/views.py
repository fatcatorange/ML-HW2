from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from transformers import AutoTokenizer, AutoModel
import json
import torch

from django.http import JsonResponse

torch.device('cpu')

@csrf_exempt
def generate_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        if not prompt:
            return JsonResponse({'status': False, 'message': 'prompt 不能為空'}, status=400)
        try:
            tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
            print(prompt)
            model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()
            model = model.eval()
            response, history = model.chat(tokenizer, prompt , history=[])
            print(response)
            response_text = response
        except Exception as e:
            print(e)
            return JsonResponse({'status': False, 'message': '錯誤'}, status=500)
        return JsonResponse({'status': True, 'data': {'response': response_text}})
    else:
        return JsonResponse({'status': False, 'message': '只能用 POST'}, status=405)

