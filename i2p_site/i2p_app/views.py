from datetime import datetime
from django.shortcuts import render
# from django.shortcuts import redirect
# from django.http import HttpResponseRedirect

import replicate
import requests
from datetime import datetime
from django.core.files.storage import FileSystemStorage

model = replicate.models.get("pharmapsychotic/clip-interrogator")
version = model.versions.get("a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90")


def home(request):

    if request.method == 'POST' and 'image_link' in request.POST:
        
        image_link = request.POST['image_link']
        image_name = str(datetime.now())[:19].replace(' ', '-').replace(':', '-')

        img_data = requests.get(image_link).content
        with open(f'./images/{image_name}.jpg', 'wb') as handler:
            handler.write(img_data)


        inputs = {
            'image': open(f'./images/{image_name}.jpg', "rb"),

            # Choose ViT-L for Stable Diffusion 1, and ViT-H for Stable Diffusion
            'clip_model_name': "ViT-L-14/openai",

            # Prompt mode (best takes 10-20 seconds, fast takes 1-2 seconds).
            'mode': "best",
        }

        output = version.predict(**inputs)
      
        return render(request, 'home.html', {
            'prompt': output,
        })

        # return redirect('/', {'prompt': output})
    
    elif request.method == 'POST':
        image_user = request.FILES['image_user']
        fs = FileSystemStorage()
        image_name = str(datetime.now())[:19].replace(' ', '-').replace(':', '-')
        filename = fs.save(f'./images/{image_name}.jpg', image_user)

        inputs = {
            'image': open(f'./images/{image_name}.jpg', "rb"),

            # Choose ViT-L for Stable Diffusion 1, and ViT-H for Stable Diffusion
            'clip_model_name': "ViT-L-14/openai",

            # Prompt mode (best takes 10-20 seconds, fast takes 1-2 seconds).
            'mode': "best",
        }

        output = version.predict(**inputs)

        return render(request, 'home.html', {
            'prompt': output,
        })
    
    
    else:
        return render(request, 'home.html', {
            'prompt': '--',
        })