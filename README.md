# syu_likelion_renewal
## 멋쟁이사자처럼 삼육대학교 2020 홈페이지 리뉴얼

## 기존에 존재했던 삼육대학교 멋사 홈페이지인 http://sahmyook.likelion.org/ 의 편의성과 효율성을 개편하고자 리뉴얼 프로젝트를 시작하게 되었습니다. ####

인원 : 이정은, 김지윤, 노동준, 윤채린, 최정은

# 초기셋팅

1. git clone을 합니다.  `git clone https://github.com/SYULION8TH/syu_likelion_renewal.git`

2. 가상환경을 생성해줍니다.  `python -m venv myvenv`

3. 가상환경을 실행해니다. 윈도우 : ` source myvenv/Scripts/activate` 맥os : `source myvenv/bin/activate`

4. 저희는 장고환경에서 할겁니다. 그럼 pip install해야겠죠? `pip install -r requirements.txt`

5. 설치가 완료되었으면 `python manage.py runserver` 이후 `127.0.0.1:8000/admin` 으로 들어가서 제대로 되었는지 확인해줍니다. 
 
 >- id : syu
 >- pw : 123
 
 초기셋팅 끝! 
 
 
 # 구조 안내
 
 저희가 구현할 총 기능 목록은
 
 1. main(동아리원, 서비스, 서비스 상세)
 
 2.타임라인, 타임라인 상세
 
 3.오류위키(오류위키 글쓰기, 게시글 목록, 게시글 상세, 해시태그 쓰기)
 
 4.해시태그(해시태그 순위) => 모듈화
 
 5.토론(토론 목록, 토론 상세, 토론 상세 의견)  
 
 으로 나눌 수 있습니다. 
 
 
  파일구조는 `likelion_syu_renewal` 이것이 프로젝트 폴더
  나머지 `main` `timeline` `errorwiki` `discussion` 총 4개가 앱 폴더입니다.
  
  
  ### 메인 - 
   
  ### 타임라인 - 
  ### 오류위키 - 
  ### 토론 - 
  
  # 각 기능에 맞게 앱 폴더 범위 안에서만 작업해주세요! 아래 사항 꼭 모두 숙지해주세요!
  
  ### css와 js파일은 되도록 html파일에 우겨넣지 마시고 각 앱의 templates/static 폴더에 알맞게 넣어서 적용시켜주세요!
  ### static폴더는 static파일들이 들어가는 곳입니다!(css,js,img파일 등등..) 각 폴더의 용도에 맞는 파일만 넣어주세요!
  ### 모든 db는 main/models.py에 존재합니다!
  ### 작업중 static파일이 변경되면 결과를 보기전에 `python manage.py collectstatic` 하는거 잊지 맙시다! static파일들이 모이는 중앙 static폴더 위치는 likelion_syu_renewal/static
  
  
  
