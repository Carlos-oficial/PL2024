from typing import List, Dict
import sys, os, json


def csv_to_list(f_path: str) -> List[Dict[str, str]]:
    res = list()
    with open(f_path) as f:
        lines: List[str] = f.readlines()
        keys: List[str] = lines[0].rstrip().split(",")
        for line in lines[1:]:
            line: str = line.rstrip()
            res.append(dict(zip(keys, line.split(","))))
    return res


def main(f_path):
    l = csv_to_list(f_path)

    n_atletas = len(l)

    min_idade = int(min(l, key=lambda x: x.get("idade")).get("idade"))
    max_idade = int(max(l, key=lambda x: x.get("idade")).get("idade"))
    escaloes = list(
        zip(range(min_idade, max_idade, 5), range(min_idade, max_idade, 5)[1:])
    )

    atletas_por_escalao = {
        escalao: len(
            list(
                filter(
                    lambda x: (
                        int(x.get("idade")) < escalao[1]
                        and int(x.get("idade")) >= escalao[0]
                    ),
                    l,
                )
            )
        )
        / n_atletas
        for escalao in escaloes
    }

    atletas_aptos = (
        len(list(filter(lambda x: (x.get("resultado") == "true"),l,)))
        / n_atletas
    )
    modalidades = sorted(list({v.get("modalidade") for v in l}))
    print(modalidades)
    print(atletas_aptos * 100,"%")
    print(atletas_por_escalao)


if __name__ == "__main__":
    main(sys.argv[1])
