from docxtpl import *

def create_CV_using_my_word_template(FIO, birth_date, location, languages, salary, jobs_return, educations_return, \
                                     additional_educations_return):

    # doc = DocxTemplate("h://Работа/headhunting/createCV/my_word_template.docx")
    doc = DocxTemplate("my_word_template.docx")
    context = { 'ФАМИЛИЯ_ИМЯ_ОТЧЕСТВО' : FIO.upper(),
                'ДАТА_РОЖДЕНИЯ' : birth_date,
                'МЕСТО_ЖИТЕЛЬСТВА' : location,
                'ЗАРПЛАТНЫЕ_ОЖИДАНИЯ' : salary}

    # 'ДАТА_РАБОТЫ': job["date"],
    # 'НАЗВАНИЕ_КОМПАНИИ': job["name"],
    # 'НАЗВАНИЕ_ДОЛЖНОСТИ': job["position"],
    # 'ПУНКТ_ОПИСАНИЯ_ДОЛЖНОСТИ': Listing(
    #     job_description),  # Кафедра теоретической физики \n• И еще какая-то кафедра \n• И еще какая-то, более длинная кафедра"),
    # # 'ПУНКТ_ОПИСАНИЯ_ДОЛЖНОСТИ' : Listing("• " + job["description"][0] + "\n• " + job["description"][1]), # Кафедра теоретической физики \n• И еще какая-то кафедра \n• И еще какая-то, более длинная кафедра"),
    # 'ДАТА_ОБРАЗОВАНИЯ': education["date"],
    # 'НАЗВАНИЕ_ВУЗА': education["name"],
    # 'НАЗВАНИЕ_ФАКУЛЬТЕТА': education["facultee"],
    # 'ДАТА_ДОП_ОБРАЗОВАНИЯ': additional_education["date"],
    # 'НАЗВАНИЕ_ДОП_ОБРАЗОВАНИЯ': additional_education["name"],
    # 'ОПИСАНИЕ_ДОП_ОБРАЗОВАНИЯ': additional_education["description"]

    # JOBS
    for i in range(0,len(jobs_return)):
        j = jobs_return[i]
        try:
            # jj = j["description"]
            # job_bullets = jj.split(". ")
            # job_bullets = str(j['description']).split("\n")
            # job_description = "• " + job_bullets[0] + "\n"
            job_description = j["description"]
            # for i2 in range(1, len(job_bullets)):
                # job_description = job_description + "• " + job_bullets[i2] + "\n"
        except KeyError:
            job_description = ""

        context.update({'ДАТА_РАБОТЫ_' + str(i+1): j["date"].replace("настоящее время","н.в.")})
        context.update({'НАЗВАНИЕ_КОМПАНИИ_' + str(i+1): j["name"]})
        context.update({'НАЗВАНИЕ_ДОЛЖНОСТИ_' + str(i+1): j["position"]})
        context.update({'ПУНКТ_ОПИСАНИЯ_ДОЛЖНОСТИ_' + str(i+1): Listing(job_description)})
        # 'НАЗВАНИЕ_КОМПАНИИ': job["name"],
        # 'НАЗВАНИЕ_ДОЛЖНОСТИ': job["position"],
        # 'ПУНКТ_ОПИСАНИЯ_ДОЛЖНОСТИ': Listing(
        #     job_description),  # Кафедра теоретической физики \n• И еще какая-то кафедра \n• И еще какая-то, более длинная кафедра"),
        # 'ПУНКТ_ОПИСАНИЯ_ДОЛЖНОСТИ' : Listing("• " + job["description"][0] + "\n• " + job["description"][1]), # Кафедра теоретической физики \n• И еще какая-то кафедра \n• И еще какая-то, более длинная кафедра"),

    # EDUCATIONS ##################################################################################

    for i in range(0,len(educations_return)):
        e = educations_return[i]
        context.update({'ДАТА_ОБРАЗОВАНИЯ_' + str(i+1): e["date"].replace("настоящее время","н.в.")})
        context.update({'НАЗВАНИЕ_ВУЗА_' + str(i+1): e["name"]})
        context.update({'НАЗВАНИЕ_ФАКУЛЬТЕТА_' + str(i+1): e["facultee"]})
        # context.update({'ОПИСАНИЕ_ОБРАЗОВАНИЯ_' + str(i+1): Listing(education_description)})
        context.update({'ОПИСАНИЕ_ОБРАЗОВАНИЯ_' + str(i+1): educations_return[i]["description"]})

    # ADDITIONAL EDUCATIONS #######################################################################

    for i in range(0,len(additional_educations_return)):
        additional_e = additional_educations_return[i]
        context.update({'ДАТА_ДОП_ОБРАЗОВАНИЯ_' + str(i+1): additional_e["date"].replace("настоящее время","н.в.")})
        context.update({'НАЗВАНИЕ_ДОП_ОБРАЗОВАНИЯ_' + str(i+1): additional_e["name"]})
        context.update({'ОПИСАНИЕ_ДОП_ОБРАЗОВАНИЯ_' + str(i+1): additional_e["description"]})

    # LANGUAGES

    for i in range(0,len(languages)):
        context.update({'ЯЗЫК_' + str(i+1): languages[i]["language"] + ":"})
        context.update({'УРОВЕНЬ_ЯЗЫКА_' + str(i+1): languages[i]["level"]})

    # PHOTO
    try:
        doc.replace_pic('default_userpic.jpg',"imgs/" + FIO.upper() + ".jpg")
    except:
        print("no photo")

    # RENDER & SAVE
    doc.render(context)
    doc.save("docxs/" + FIO.upper() + ".docx")

