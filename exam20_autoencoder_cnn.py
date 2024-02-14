# 오토엔코더가 엔코딩을 하면 이미지의 특성만 남음. 압축을 했다가 이미지 사이즈를 복원을 하면 다시 원래 사이즈로 돌아감. 이것이 오토엔코더를 쓴거야.

# 특성 학습을 했을 때(EX 목격자(=오토인코더를 의미) 가 하는 진술을 바탕으로 몽타주를 그리는 사람(=오토인코더의 후 작업을 의미해) 이 있어. 목격자의 진술을 바탕으로 특성을 기억해.
# 그 후 그 특성을 바탕으로 그림을 그려내.

# 저해상도 이미지를 입력했을 때 고해상도 이미지를 출력할 수 있어. (-> 왜?)
# ex) 소설의 요약집을 보고, 줄거리만을 보고 나의 이야기를 쓸 수 있어. 그대신 학습한 것만 된다.

# 이미지의 잡음(?) 조사를 할 수 있어. -> 노이즈 (?)
# ex) 밤에 도둑이 들어왔는 데 잡음이 들어왔는 데도 깨끗한 이미지로 복원이 가능해. 그런데 학습된 이미지여야해 (회사동료라던지...). 학습이 안된 데이터는 이미지를 출력할 수 없어.

# 오토엔코더를 cnn layer를 이용해서 마지막으로 이용을 함.


#-> encoded= MaxPool2D  # 4X4는 아임쇼를 가지고 그려볼 수 있어.
#->  upsampling과 Maxpool2D의 차이점 기억하기.


# 사이클단위(?)시즌 단위(?) ---> 이거 아닌 듯. ex) 봄에 찍은 내용을 겨울로 바꿔 줄 수 있어, 같은 장소를 계절감만 바꿔서 해줄 수 있어.
# 엔코더와 디코더부분을 따로 떼서 해줄 수 있을 거라고 생각했습니다-> 그런데 안됐습니다. 왜냐면 학습한 것만 가능해. 이것은 새로운 것을 만들어내는 것이니까 안된다. 그래서 오토엔코더는 의미 없다.
# 봄에 찍은 사진을 겨울로 바꾸는 작업은 주로 이미지 변환(Image Translation) 작업에 해당합니다. 이런 작업을 수행하기 위해서는 오토인코더보다는 Generative Adversarial Network (GAN)이나 Variational Autoencoder (VAE) 등의 생성 모델이 더 효과적일 수 있습니다.
# Generative Adversarial Network (GAN): GAN은 생성자(Generator)와 판별자(Discriminator)라는 두 신경망으로 이루어진 구조입니다. 생성자는 입력으로부터 새로운 이미지를 생성하고, 판별자는 생성자가 만든 이미지와 실제 이미지를 구별합니다. 학습이 진행되면서 생성자는 판별자를 속이기 위해 더 실제 같은 이미지를 생성하게 되어 원하는 계절로의 이미지 변환을 수행할 수 있습니다.
# Variational Autoencoder (VAE): VAE도 오토인코더의 변종 중 하나로, 확률적 잠재 변수를 사용하여 입력 데이터를 표현합니다. VAE는 이미지를 생성하는 데에도 사용될 수 있고, 특히 이미지의 잠재 변수를 조절하여 다양한 스타일이나 특징을 가진 이미지를 생성할 수 있습니다.
# Conditional Generative Models: 조건부 생성 모델은 특정 조건을 부여하여 이미지를 생성하는 방식입니다. 예를 들어, 원하는 계절을 조건으로 주고 해당 계절에 맞는 이미지를 생성하도록 학습시킬 수 있습니다.
# 이러한 모델들은 훈련 과정을 거쳐 적절한 학습 데이터를 기반으로 이미지를 생성하거나 변환할 수 있습니다. 선택한 모델에 따라 학습 데이터와 모델 구조를 조정하여 봄에서 겨울로의 이미지 변환을 성공적으로 수행할 수 있습니다.

# openAi 에 '다리'(=말하는 것을 그림으로 그려줘) 라고 하는 것 있음. '스테이브 디퓨전'(=이미지를 이미지로 만들어줌.)

# 지피티를 우리가 만들어야하는 이유? 회사 안에서의 프로젝트가 공유 될 수도있으니까, 회사만의 지피티를 만들어야한다.
