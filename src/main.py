import keqing

def main(element_id:str):
    flag_mode="online" #local

    wt_file=open("template.wikitext","r",encoding="utf-8")
    wt_content=wt_file.read()
    wt_file.close()

    map=keqing.Waifu()
    if flag_mode == "online":
        map.read_network(
            server="OGF",
            quantity="element",
            type="way",
            element_id=element_id,
        )
    else:
        map.read(mode="f", fpath="")
    
    map.meow()
    


if __name__ == "__main__":
    main("")