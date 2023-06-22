import keqing


def main(element_id: str):
    flag_mode = "online"  # local

    wt_file = open("template.wikitext", "r", encoding="utf-8")
    wt_content = wt_file.read()
    wt_file.close()

    map = keqing.Waifu()
    if flag_mode == "online":
        map.read_network(
            server="OGF",
            quantity="element",
            type="way",
            element_id=element_id,
        )
    else:
        map.read(mode="f", fpath="")

    # 假设只有一条路

    for id in map.way_dict:
        node_list = map.way_dict[id].nds
    for id in node_list:
        map.read_network(
            server="OGF",
            quantity="element",
            type="node",
            element_id="n" + str(id),
        )

    # map.meow()
    pos_list = []
    for id in map.node_dict:
        pos_list.append((map.node_dict[id].lat, map.node_dict[id].lon))

    lat_list = [i[0] for i in pos_list]
    lon_list = [i[1] for i in pos_list]
    max_lat = max(lat_list)
    min_lat = min(lat_list)
    max_lon = max(lon_list)
    min_lon = min(lon_list)
    center = (
        str(max_lat * 0.5 + min_lat * 0.5)
        + ","
        + str(max_lon * 0.5 + min_lon * 0.5)
    )
    zoom = 7
    line = " :".join([str(i[0]) + "," + str(i[1]) for i in pos_list])

    wt_content=wt_content.replace("{{center}}", center).replace(
        "{{zoom}}", str(zoom)
    ).replace("{{line}}", line)
    print(wt_content)


if __name__ == "__main__":
    main("w30343467")
