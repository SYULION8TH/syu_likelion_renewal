
# 멋쟁이사자처럼 삼육대학교 2020 홈페이지 리뉴얼

## 참여인원

 - 서버 : 이정은, 김지윤, 노동준, 윤채린, 최정은
 - 클라이언트 : 김혜원, 김민상, 류지윤, 성예지, 양유림 

## 초기셋팅

1. git clone을 합니다.  `git clone https://github.com/SYULION8TH/syu_likelion_renewal.git`

2. 가상환경을 생성해줍니다.  `python -m venv myvenv`

3. 가상환경을 실행합니다. 윈도우 : ` source myvenv/Scripts/activate` 맥os : `source myvenv/bin/activate`

4. 저희는 장고환경에서 할겁니다. 그럼 pip install해야겠죠? `pip install -r requirements.txt`

5. 설치가 완료되었으면 `python manage.py runserver` 이후 `127.0.0.1:8000/admin` 으로 들어가서 제대로 되었는지 확인해줍니다. 
 
 >- id : syu
 >- pw : 123
 
 초기셋팅 끝! 
 
 >  pip install 시에 mysqlclient 관련 에러가 발생한다면 다음 [링크](https://victorydntmd.tistory.com/275) 혹은 설명을 참고해주세요
 
 ### mysqlclient 에러
 
 1. 터미널에서 `python --version` 명령어를 이용해 버전을 확인해줍니다
 
 2. [링크](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)에서 `mysqlclient‑1.4.6‑cp[본인 버전]‑cp[본인 버전]‑win32.whl`에 해당하는 파일을 다운로드 받아줍니다. 접근이 편하도록 `c:\`같은 폴더에 다운로드 받아줍시다
 > 만약 버전이 `3.8.3`라면 `mysqlclient-1.4.6-cp38-cp38-win32.whl` 파일을 다운로드 받아주시면 됩니다
 
 3. 터미널 혹은 `bash`, `powershell`을 이용해 다운로드 받은 경로 (위의 경우라면 `c:\`)에 접근한 후 `pip install mysqlclient-1.4.6-cp{본인 버전}-cp{본인 버전}-win32.whl`을 입력해주세요
 
 4. 설치가 완료되고난 후, 다시 프로젝트 폴더로 이동해 `pip install -r requirements.txt`를 실행해주세요
 
 5. 끗-!
 
 ## 구조 안내
 
  파일구조는 `likelion_syu_renewal` 이것이 프로젝트 폴더
  나머지 `main` `timeline` `errorwiki` `discussion` 총 4개가 앱 폴더입니다.
  
  ## 브랜치 생성 
  
  
  ## Back-end 업무 목록
  
  #### 메인 - 노동준
   - 구성원 목록
   - 서비스 목록
   - 서비스 상세 
   
  #### 타임라인 - 윤채린
   - 타임라인 목록
   - 타임라인 상세 (jsonResponse)
   
  #### 오류위키 - 최정은 
   - 게시글 작성
   - 게시글 목록
   - 게시글 상세
   - 해시태그 
   
  #### 토론 - 김지윤 
   - 토론 목록
   - 토론 상세
   - 토론 의견 
  
 ## Front-end 업무 목록 
 
  ## 각 기능에 맞게 앱 폴더 범위 안에서만 작업해주세요! 아래 사항 꼭 모두 숙지해주세요!
  
  - css와 js파일은 되도록 html파일에 넣지 마시고 각 앱의 templates/static 폴더에 알맞게 넣어서 적용시켜주세요.
  - static폴더는 static파일들이 들어가는 곳입니다!(css,js,img파일 등등..) 각 폴더의 용도에 맞는 파일만 넣어주세요.
  - 모든 db는 main/models.py에 존재합니다.
  - 작업중 static파일이 변경되면 결과를 보기전에 `python manage.py collectstatic` 하는거 잊지 맙시다! static파일들이 모이는 중앙 static폴더 위치는 likelion_syu_renewal/static
  
  
  
