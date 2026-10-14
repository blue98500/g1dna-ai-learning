# G1DNA 프로젝트 관리 프로그램 v1
import json
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
        print(번호, p["name"], p["status"])
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

#====== 메뉴 실행 ====== 
projects = load_projects()

while True:
    print("\n=== G1DNA 프로젝트 관리 ===")
    print("1.목록  2.추가  3.검색  4.삭제  0.종료")
    menu = input("번호 선택: ")

    if menu == "1":
        show_projects(projects)

    elif menu == "2":
        name = input("현장 이름: ")
        area = int(input("면적(m2): "))
        budget = int(input("예산(원): "))
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

    else:
        print("없는 번호입니다.")
    