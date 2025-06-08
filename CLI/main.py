from app.db.controller import create_project


def main():
    state = 0
    
    while(True):
        if state == 0:
            print('1 - create new project post')
            print('2 - edit project post !!COMING SOON!!')
            print('3 - delete project post !!COMING SOON!!')
            print('0 - exit')
            
            inp = int(input())
            if inp == 0: break
            if inp == 1: state = 1
        
        if state == 1:
            img_urls = []
            for i in range(4): 
                print(f'Enter the image url[{1}] (or None)')
                tmp_img_url = input()
                if tmp_img_url is not 'None':
                    img_urls.append(input())

            print(f'Enter the title of project')
            title = input()

            print(f'Enter the client of project')
            client = input()

            print(f'Enter the category of project')
            category = input()

            print(f'Enter the date of project')
            date = input()

            print(f'Enter the project url')
            project_url = input()

            print(f'Enter the subtitle of project')
            subtitle = input()

            print(f'Enter the description of project')
            description = input()
            
            create_project(img_urls, title, client, category, date, project_url, subtitle, description)
            

if __name__ == '__main__':
    main()