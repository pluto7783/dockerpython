# django_msa_study
# prerequisite
- koo-eks.pem

## 개인 jumpbox 접속
- 대희 : 52.14.194.51
- 민수 : 3.15.185.77
- 지윤: 18.118.115.240
- 찬: 3.141.100.142 (new)
- 소언: 18.118.23.72 (new)
- 소연: 18.117.118.202
- 종철: 3.144.178.188 ( new )


## 1. ec2 접속

- 카톡으로 제공드린 pem키 이용하여 접속

## 2. 새로운 k8s 클러스터의 config 등록
- 제공받은 kubeconfig를 .kube 폴더의 config 라는 이름으로 저장합니다.
- 기존에 eks에 사용했던 config는 config.old로 이름을 바꿔둡니다.

## 3. django를 docker 기반으로 빌드해놓은 어플리케이션을 확인합니다.
```
git clone https://github.com/themapisto/django_msa_study.git
```

## 4. 접속
- 자기아이피:8000
