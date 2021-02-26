# aes.py

파이썬을 이용한 보안 테스트코드


openssl을 이용한 암호화 복호화 테스트


AES - CBC알고리즘, CTR알고리즘을 이용하여 암호화 혹은 복호화


utf-8 형식 사용하여 한글지원

----------------------------------------
**[Commands]**

-h or -help : 사용법 설명

----------------------------------
**[사용법]**

python3 aes.py [dec/enc] [cbc/ctr] [key파일] [iv파일] [입력파일] [출력파일]


* dec/enc - 암호화 혹은 복호화 선택
    * 암호화모드 : enc
    * 복호화모드 : dec
* cbc/ctr - 알고리즘 선택
    * CBC알고리즘 사용 : cbc
    * CTR알고리즘 사용 : ctr
* key 파일 - 암호화 혹은 복호화 할때 사용할 key값이 있는 파일명
* iv 파일 - 암호화 혹은 복호화 할때 사용할 iv값이 있는 파일 명
* 입력파일 - 암호화 혹은 복호화할 파일명
* 출력파일 - 출력할 파일 명

----------------------------------
**[사용예시]**

1. input.txt파일을 output.txt파일로 암호화 하려 할때
    - cbc 알고리즘 사용
    - 키값을 key.txt 파일 이용
    - iv값을 iv.txt 파일 이용

    `$ python3 aes.py enc cbc key.txt iv.txt input.txt output.txt`

>aes.py 없이 openssl 프로그램을 사용하면 다음의 명령어와 같다.(단 iv는 직접 데이터를 입력해야한다.)
>
>$openssl enc -e -aes-128-cbc -kfile key.txt -iv ivdata -in input.txt -out output.txt

2. input.txt파일을 key.txt와 iv.txt를 이용하여 output.txt파일로 복호화 하려 할때
    - ctr 알고리즘 사용
    - 키값을 key.txt 파일 이용
    - iv값을 iv.txt 파일 이용
    
   
    `$ python3 aes.py dec ctr key.txt iv.txt input.txt output.txt`

>aes.py 없이 openssl 프로그램을 사용하면 다음의 명령어와 같다.(단 iv는 직접 데이터를 입력해야한다.)
>
>$openssl enc -d -aes-128-ctr -kfile key.txt -iv ivdata -in input.txt -out output.txt


----------------------------------
**[KEY파일과 iv파일 제작법]**


- openssl 프로그램을 사용합니다.

- rand 명령어를 사용하여 랜덤 수 제작 

- '-hex' 명령어를 추가하여 랜덤 수를 16진수로 제작

- '>>'명령어를 이용하여 파일에 저장


*  예시
  
```
$ openssl rand -hex 16 >> key.txt

$ openssl rand -hex 16 >> iv.txt
```

----------------------------------
**[필요한 라이브러리]**


pyopenssl
pycryptodome