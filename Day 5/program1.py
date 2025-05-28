with open('programs.txt','w') as file:
    para='In the heart of the bustling city, hidden between\n towering skyscrapers and busy streets, lies a small, peaceful park. \nHere, the sound of chirping birds and rustling leaves creates a soothing escape from \nthe urban rush. People come to this oasis to relax, read books, or simply \nenjoy the fresh air. The park changes with the seasons, from vibrant blossoms in spring to golden leaves in \nautumn. It’s a reminder that even in the busiest places, nature finds a way to thrive and bring calm to our lives.In the heart of the bustling city, hidde\nn between towering skyscrapers and busy streets, lies a small, peaceful park. Here, the sound of chirping birds and rustling leaves creates a soothing escape from the urban rush. People come to this oasis to relax, read books, or \nsimply enjoy the fresh air. The park changes with the seasons, from vibrant blossoms in spring to golden leaves in autumn. It’s a reminder that even in the busiest places, nature finds a way to thrive and bring calm to our lives.'
    file.write(para)
#total number of lines in file
with open('programs.txt','r') as file:
    total_lines=file.readlines()               #we can direct iterate without using readlines -->   for f in file
    count=0
    char_count=0
    words=[]
    for line in total_lines:
        char_count+=len(line)
        line=line.split()
        words.extend(line)
        count+=1
    total_words=len(words)
    print("total characters: ",char_count)
    print("total_words: ",total_words)
    print("total number of lines : ",count)
