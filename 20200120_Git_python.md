# 20200120

## 1. git-소스코드관리도구.

https://backlog.com/git-tutorial/kr/intro/intro1_1.html- 한글설명서

버전관리를 통해서 소스코드를 관리한다. (디렉토리(폴더) 중심.)

나의 코드관리도구, 팀의 코드 협업도구.

scm(source code management tool) what == vcs(version) how

```sequence
mycomputer->Github: git push
team->Github: 팀소스코드
```





> [리누스 토르발스](https://namu.wiki/w/리누스 토르발스)가 개발한 분산형 [버전 관리 시스템](https://namu.wiki/w/버전 관리 시스템)(VCS).
>
> Git은 매우 빠른 속도와 분산형 저장소 지원이 특징이다. 방대한 [리눅스](https://namu.wiki/w/리눅스) 커널 소스 코드를 생각해 보면, 속도 문제는 매우 중요하다. 오픈 소스 개발의 특성상 여럿이 달려들어 자기 맘에 드는 걸 하기도 하며, 또한 뭘 하나 잘못 붙였다 이상한 걸 건드려 망하기 쉬운데, Git는 이런 환경의 특성에 맞게끔 잘 만들어져 있다.

```
# 설치, 버전확인
git --version
git version 2.25.0.windows.1
```

#### TIL(today i learned)

john resig가 처음 시작..

```
$ git init
multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL (master) #깃으로 관리되는 폴더.
$ rm -r #폴더 지우기. #git stop 버전들이 사라지고 최종버전만 남음.
multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL 
$ git status #상태체크
```

#### version관리

commit = 저장하다(staging area, index)

version은 = snapshot

- `add`(staging - **선택**할 수 있다. `add .`은 되도록 피하기.)
- `add -u` : 파일 삭제, 변화 상황에 대한 명령어.



```
$ git add a.txt # 파일 또는 폴더명
$ git config -- global user.email "dmdekf@gmail.com"
$ git config -- global user.name "dmdekf"
$ git config --global --list
user.email=dmdekf@gmail.com
user.name=dmdekf
```

- `commit` - do!!

```
$ git commit "" # 아무것도 적지 않을 경우 vim editor 로.. 
$ git commit -m "first commit" #message는 -m 주로 버전사이의 변화를 나타내는걸로 하자.
[master (root-commit) bd85568] first commit
 1 file changed, 171 insertions(+)
 create mode 100644 00_markdown_basic.md
$ git log # commit history
commit bd8556879f8b17a7f87afd352c8f9b82f6f01ed9 (HEAD -> master)
Author: dmdekf <dmdekf@gmail.com>
Date:   Mon Jan 20 09:52:30 2020 +0900

    first commit
```

#### commit Message.!!!

```
[Go: Update generated wrapper functions for TensorFlow ops.]
[tensorflower-gardener]
```

- `git log --oneline`  git log 간단하게 표현.

```
$ git log --oneline
17e5e4c (HEAD -> master) Add a.txt
bd85568 first commit
```

- `checkout` commit 특정 식별자 로 이동.(헥사코드)... 이동한 후에는 아무것도 하지 말자..되도록. (폴더상태가 특정 커밋상태로 변화. )

```
$ git checkout bd85568
multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL ((bd85568...)) # 특정 커밋의 상태 확인.
$ git checkout master # 원 상태 커밋으로 돌아오기.
multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL (master)

```

- `remote` (원격저장소 연결 )`add` (저장소 추가) `저장소의 이름(별명)` `저장소의 주소`

```
$ git remote add origin https://github.com/dmdekf/TIL.git
$ git remote -v
origin  https://github.com/dmdekf/TIL.git (fetch)
origin  https://github.com/dmdekf/TIL.git (push)


```

- `push` 저장소 이름 master

```
$ git push origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 2.22 KiB | 2.22 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/dmdekf/TIL.git
 * [new branch]      master -> master


```

### 여러 장소에서 github이용하기.

#### (1) 내컴퓨터 <-> 멀티캠

새로운 장소 : `clone` 저장소주소

 `pull origin master` : git hub 의 상태로 update

```
$ git status
On branch master
nothing to commit, working tree clean #working tree clean메세지가 있을 때 pull 해야 오류방지.

```



`push origin master` : git hub로 commit 을 완료함.

기존 장소의 폴더: `pull origin master`

```
$ git remote -v 
origin  https://github.com/dmdekf/TIL.git (fetch)
origin  https://github.com/dmdekf/TIL.git (push)
$ git push origin master
$ git pull origin master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (3/3), 285 bytes | 35.00 KiB/s, done.
From https://github.com/dmdekf/TIL
 * branch            master     -> FETCH_HEAD
   74f0174..39571cc  master     -> origin/master
Updating 74f0174..39571cc
Fast-forward
 01_Github_TIL.md | 6 +-----
 03_python.md     | 0
 2 files changed, 1 insertion(+), 5 deletions(-)
 create mode 100644 03_python.md


```

```
git credientioal reject

protocol=https

host=lab.ssafy.com
```

초기화코드.

#### (2) 협업 내컴퓨터 <-> 팀원컴퓨터

github - settings - collaborators - user.id or user.email추가.

https://github.com/scl2589/wordchain/invitations 혹은 이메일 확인하여 수락.

#### (3) git hub 이용법

- git issue

문제점 남기기

- git Pull requests

나의 code contribute 제안사항. -> git fork, clone

```sequence
다른사람원격저장소 -> 내원격저장소:Fork 코드소스를 복제한 내 원격저장소
나의 repo->내원격저장소: pull & push
```

#### (4)  git lab

- ```ba
    622  git log --oneline --graph
    623  git branch yunji
    624  git branch
    625  git status
    626  git switch yunji
    627  git status
    628  git add .
    629  code .
    630  git status
    631  git commit -m "Add swea_d1,d2,d3"
    632  git switch master
    633  git status
    634  git switch yunji
    635  git push origin yunji
    636  git switch master
    637  git branch -d yunji
    
  ```

- 



다른폴더 건드리지 말기
master x
나만의 브랜치 만들기 - 분리된 세계다. 망하면 날리고 마스터에서 풀로 갖오기.

#### **Branching 분리된 세계/일회용!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!** 습관 들이기.

#### **branch 는 원래 평등**하다. 하지만 `master`가 주가 되도록 커밋을 해야 중심을 잡기 쉽다. 

release branches == test branches  

feature branches ex) login, ... 등등 기능의 구현 브랜치로 일회성이 많다. 

![git-flow_overall_graph](assets/git-flow_overall_graph.png)

```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (master)
$ git branch
* master

multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (master)
$ git branch yunji

multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (master)
$ git branch
* master
  yunji

multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (master)
$ git switch yunji
Switched to branch 'yunji'

multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (yunji)

multicampus@DESKTOP-KVCQHCD MINGW64 ~/goldenbell (master)
$ git branch -d yunji
Deleted branch yunji (was 1eb7c43).
#브랜치 만들면서 이동하기. git switch -c yunji == git checkout -b yunji
multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (master)
$ git switch -c yunji

Switched to a new branch 'yunji'

multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (yunji)



```

#### merge  주체가 되는 브랜치로 이동 후 !!! master

**branch 는 원래 평등**하다. 하지만 `master`가 주가 되도록 커밋을 해야 중심을 잡기 쉽다. 



![image-20200205134444948](assets/image-20200205134444948.png)

1. FF-merge(git이 자동으로 merge) - Auto (개별 브랜치들이 충돌하지 않을 때.)

   파일 간 충돌이 없을 때. 커밋의 내용이 다른 파일들 혹은 파일 내의 수정이 없는 경우.

   commit에  merge로그 남기는 것이 default

   ```bash
   $ git log --oneline
   24e874a (HEAD -> master) Merge branch 'yunji'
   
   ```

2. Merge conflict - 두가지 진실일 때만. 

![image-20200205135820601](assets/image-20200205135820601.png)

```bash
CONFLICT (add/add): Merge conflict in README.md
Auto-merging README.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both added:      README.md
$ git commit -m "Resolve comflicts"
```



```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (yunji)
$ git switch master
Switched to branch 'master'

multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (master)
$ git merge yunji
Updating f90bdee..3a6774b
Fast-forward
 c.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 c.txt

```

#### branch는 일회용. 지우기

```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (master)
$ git branch -d yunji
Deleted branch yunji (was 3a6774b).

multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (master)
$ git branch
* master

```

#### 주의사항. head - >마스터 인지 확인하기.

```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/branching (master)
$ git log --oneline
3a6774b (HEAD -> master) Add c.txt
f90bdee Add b.txt
2d09146 Add a.txt

```



#### request

merge

content adventing? 

deep copy가 아닌 작업물만 copy..









## 2. Python

`cp`  ''복사할 파일의 주소''  ''복사할 장소''

#### jupyter notebook

```
$ pip install jupyter

$ jupyter notebook # 주피터노트북 열기

```

Y: change cell to code

M: change cell to markdown



A: insert cell above

B: insert cell below

X: cut selected cells

C: copy selected cells

Shift-V: paste cells above

V: paste cells below

Z: undo cell deletion

D,D: delete selected cells

### PEP 8 -- Style Guide for Python Code

>  **coding conventions** : 코딩 스타일 규칙
>
> Guido van Rossum <guido at python.org>, Barry Warsaw <barry at python.org>, Nick Coghlan <ncoghlan at gmail.com>

#### bool

> `False`로 변환됩니다. **완전히 부정할 수 없다면 True다**.
>
> ```
> 0, 0.0, (), [], {}, '', None
> ```

## Tip

칸아카데미 크립토강의

`Python`언어를 쓰는 가장 큰 국내회사 스포카.... (도도포인트 만드는 회사) -https://www.spoqa.com/

http://pythontutor.com/

```
num = ['hello']
num2 = num
for i in num2:
    num.append(i)
    
print(num)

#무한루프...???
```

이노데이터 월터 아이작스 - 컴퓨팅 역사 관련 도서.

hiw big is sha 256 - youtube



QA팀 : pro/testors 모든 테스트를 하는 팀. 

git 연습하기사이트.

https://git-school.github.io/visualizing-git/ 