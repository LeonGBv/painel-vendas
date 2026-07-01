import pandas as pd

from mysql_conn import conectar

def processar_csv():

    caminho = 'downloads/vendas.csv'

    df = pd.read_csv(caminho, sep=';')

    conn = conectar()

    cursor = conn.cursor()

    sql = """
    INSERT INTO vendas (
        id,
        item,
        qnt,
        valor
    )
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        item = VALUES(item),
        qnt = VALUES(qnt),
        valor = VALUES(valor)
    """

    dados = [
        (
            row['id'],
            row['item'],
            row['qnt'],
            row['valor']
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(sql, dados)

    conn.commit()

    total_vendas = len(df)

    cursor.close()
    conn.close()

    return total_vendas