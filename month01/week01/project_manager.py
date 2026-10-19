# G1DNA 프로젝트 관리 프로그램 v1
import json
def ask_area():
    while True:
        text = input("면적(m²): ")
        try:
            area = float(text)
        except ValueError:
            print(" → 숫자만 입력하세요. 예 : 18.5")
            continue
        if area <= 0:
            print(" → 0보다 큰 숫자를 입력하세요.")
            continue
        return area

def ask_budget():
    while True:
        text = input("예산(원): ")
        try:
            budget = int(text)
        except ValueError:
            print(" → 정수만 입력하세요. 예 : 2000000")
            continue
        if budget <= 0:
            print("→ 0보다 큰 숫자를 입력하세요.")
            continue
        return budget

def ask_name():
    while True:
        text = input("현장명: ")
        name = text.strip()
        if name =="":
            print("→ 현장명이 비었습니다 확인 후 다시 입력하세요")
            continue
        return name


    
def add_project(projects, name, area, budget):
    """새 프로젝트를 추가하고 리스트를 돌려준다"""
    projects.append({"name":name, "area": area, "budget":budget, "status": "design"})
    return projects

def find_project(projects, keyword):
    """이름에 keyword가 포함된 프로젝트 목록을 돌려준다"""
    return [p for p in projects if keyword in p["name"]]
def show_projects(projects):
    번호 = 1
    for p in projects:
        print(번호, p["name"],p["area"],p["budget"], p["status"])
        번호 = 번호 +1
def delete_project(projects, name):
    남길것 =[]
    for p in projects:
        if p["name"] !=name: 
            남길것.append(p)
    return 남길것

def save_projects(projects):
    with open("projects.json", "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

def load_projects():
    try:
        with open("projects.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def update_projects(projects):
    show_projects(projects)
    while True:
        try :
            no = int(input("현장 번호 선택 (0:취소): "))
        except ValueError:
            print("→ 번호를 숫자로 입력하세요.")
            continue
        if no== 0:
            print("취소했습니다.")
            return
        if 1<=no<=len(projects):
            break
        print(f"→ 1 ~ {len(projects)}사이로 입력하세요.")

    target = projects[no -1]
    
    print("1)현장명 2)면적 3)예산 4) 진행상황")
    choice = input("무엇을 고칠까요?: ")

    if choice== "1":
        target["name"]=ask_name()
    elif choice=="2":
        target["area"]=ask_area()
    elif choice== "3":
        target["budget"]=ask_budget()
    elif choice=="4":
        target["status"]=input("진행상황: ").strip()
    else:
        print(" →1~4중에서 고르세요.")
        return
    
    save_projects(projects)
    print("수정 완료 →",target)



#====== 메뉴 실행 ====== 
projects = load_projects()

while True:
    print("\n=== G1DNA 프로젝트 관리 ===")
    print("1.목록  2.추가  3.검색  4.삭제  5.수정 0.종료")
    menu = input("번호 선택: ")

    if menu == "1":
        show_projects(projects)

    elif menu == "2":
        name = ask_name()
        area = ask_area()
        budget = ask_budget()
        projects=add_project(projects,name,area,budget)

    elif menu =="3":
        keyword = input("검색어: ")
        print(find_project(projects,keyword))
    

    elif menu =="4":
        name = input("삭제할 현장 이름: ")
        projects=delete_project(projects,name)

    elif menu =="0":
        save_projects(projects)
        print("저장하고 종료합니다.")
        break

    elif menu =="5":
        update_projects(projects)

    
    else:
        print("없는 번호입니다.")
    