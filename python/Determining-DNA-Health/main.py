#!/usr/bin/env python3
import sys


def newGeneNode():
    return {"c": {},
            "v": []}


def add(gene_node, gene, index, health):

    while len(gene) > 0:
        if gene[0] in gene_node["c"]:
            gene_node = gene_node["c"][gene[0]]
        else:
            gene_node["c"][gene[0]] = newGeneNode()
            gene_node = gene_node["c"][gene[0]]

        gene = gene[1:]

    gene_node["v"].append((index, health))
    return gene_node


def totalHealth(gene_node, gene, start, end):
    total_health = 0

    cur_gene_nodes = [gene_node]
    while len(gene) > 0:
        to_del = []
        to_add = []
        to_replace = []
        for cur_gene_node_i, cur_gene_node in enumerate(cur_gene_nodes):
            if gene[0] in cur_gene_node["c"]:
                next_gene_node = cur_gene_node["c"][gene[0]]

                for i, v in next_gene_node["v"]:
                    if start <= i <= end:
                        total_health += v

                if cur_gene_node_i == 0:
                    to_add.append(next_gene_node)
                else:
                    to_replace.append((cur_gene_node_i, next_gene_node))
            else:
                if cur_gene_node_i != 0:
                    to_del.append(cur_gene_node_i)

        for replace_i, replace_node in to_replace:
            cur_gene_nodes[replace_i] = replace_node
        for i, del_i in enumerate(to_del):
            cur_gene_nodes[del_i-i]
        for add in to_add:
            cur_gene_nodes.append(add)

        gene = gene[1:]
    return total_health


if __name__ == "__main__":
    input()  # n unused

    g = input().rstrip().split()
    h = map(int, input().rstrip().split())

    gn = newGeneNode()
    for i, (gene, health) in enumerate(zip(g, h)):
        add(gn, gene, i, health)
    max_h = -sys.maxsize
    min_h = sys.maxsize

    for _ in range(int(input())):
        s, e, d = input().split()
        s, e = int(s), int(e)

        th = totalHealth(gn, d, s, e)
        if th > max_h:
            max_h = th
        if th < min_h:
            min_h = th

    print(min_h, max_h)
