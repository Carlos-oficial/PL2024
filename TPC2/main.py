import sys, re, os



def main(argv: list[str]) -> None:
    
        
    
    heading = r"^(?P<heading_level>#+)\s+(?P<content>.*)"
    list_item = r"^-\s+(?P<content>.*)"
    bold = r"\*\*(?P<content>.*?)\*\*"
    italic = r"\*(?P<content>.*?)\*"
    image = r"\!\[(?P<title>.*)\]\((?P<url>.*)\)"
    link = r"\[(?P<text>.*)\]\((?P<url>.*)\)"
    
    def process_content(line):
        return line
    
    listing = False
    output = ""
    for line in sys.stdin:
        match = re.match(list_item,line)
        if match:
            if not listing:
                listing = True
                output += "<ul>\n"
            output += f"<li> {process_content(match.groupdict()['content'])} </li>\n"     
        else:
            if listing:
                listing = False
                output += "</ul>\n"
                            
            match = re.match( heading,line)
            if match:
                output += f"<h{len(match.groupdict()['heading_level'])}> {process_content(match.groupdict()['content'])} </h{len(match.groupdict()['heading_level'])}>\n"     
        
            else:
                output += f"<p>{line[:-1]}</p>\n"
        
    print (output)
if __name__ ==  '__main__':
    main(sys.argv)