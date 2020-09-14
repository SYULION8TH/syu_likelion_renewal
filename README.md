
# 멋쟁이사자처럼 삼육대학교 2020 홈페이지 리뉴얼

 SYU 멋쟁이 사자처럼 홈페이지 리뉴얼 프로젝트입니다. 

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
  
  ## GIT 운영 (필독)

각 작업자가 맡은 페이지는  [issues](https://github.com/SYULION8TH/2020-syu-club-client/issues)에서 확인할 수 있습니다. 담당자로 본인이 설정되어 있는 내용을 작업하면 됩니다. 이 때, 브랜치를 나누어 작업합니다.  
각 브랜치에서 작업한 결과물은 각 브랜치에 푸시합니다. 각 브랜치에 할당된 작업이 끝나면 dev로 pull request를 작성해 merge승인을 기다립니다.

작업은 feature -> dev -> master 의 구조로 이루어집니다.

### 1. 브랜치 유의사항

모든 작업자들은 다음과 같은 순서로 작업을 진행합니다.

1.  master  브랜치에는 작업하지 않습니다  
    
2.  기본적으로 각 기능을 개발시에는  features/#이슈번호의 브랜치를 만들어서 작업합니다 ex) features/#2
3.  작업이 완료될 때마다 해당 features브랜치로 push합니다
4.  기능 별 브랜치의 작업이 어느정도 완료된 후에는  dev로  pull request를 작성합니다

master  브랜치에는 반드시 오류가 없는 완성본들만 모아둘 예정입니다. 그렇기 때문에,  master  브랜치에는 절대 직접 작업 혹은 푸시하지 않도록 합니다. 테스트가 필요하거나 기능 개발이 완료된 경우  dev브랜치로 합치기 위해  pull request를 생성하면 담당자인 김혜원(@blair06), 이정은이 직접 머지하게 됩니다.

### 2. 커밋 메시지

커밋 메시지첫줄에 이슈번호를 반드시 붙여주세요. (예시 :  git commit -m "화면 배치 완료 #8")이렇게 작성할 경우, 이슈 목록에서 해당 커밋들을 추적할 수 있습니다. 진행사항을 체크하기 위해 반드시 첫줄에 이슈번호를 붙여주시고 나머지 커밋은 자유롭게 상세히 작성해주세요.
  
  ## Back-end 업무 목록
  
  ### 메인 - 노동준
   - 구성원 목록
   - 서비스 목록
   - 서비스 상세 
   
  ### 타임라인 - 윤채린
   - 타임라인 목록
   - 타임라인 상세 (jsonResponse)
   
  ### 오류위키 - 최정은 
   - 게시글 작성
   - 게시글 목록
   - 게시글 상세
   - 해시태그 
   
  ### 토론 - 김지윤 
   - 토론 목록
   - 토론 상세
   - 토론 의견 
  
 ## Front-end 업무 목록 
 
  ## 파일관리 
  ###파일작성요령
  
  - html명은 각자 구현할 기능 및 페이지로 표기해주세요 해당 html에서 사용되는 css명도 html과 동일한 이름을 사용합니다. ex) timeLine.html && timeLine.css
  - 상속될 템플릿(base html)을 작업하는 작업자들은 클래스명앞에 꼭 언더바 두개를 붙여 명시합니다. ex) div class="__main-navbar"
 
 ###static파일 관리
  - 각 앱의 html 파일과 css파일은 앱안의 templates폴더 안에서 관리합니다. 특히 html을 제외한 css와 js파일들은 templates/static 경로에서 관리합니다.
  - static폴더는 static파일들이 들어가는 곳입니다!(css,js,img파일 등등..) 각 폴더의 용도에 맞는 파일만 넣어주세요.
  - 모든 db는 main/models.py에 존재합니다.
  - 작업중 static파일이 변경되면 결과를 보기전에 `python manage.py collectstatic` 하는거 잊지 맙시다! 
     static파일들이 모이는 중앙 static폴더 위치는 likelion_syu_renewal/static
     
  
  
  
