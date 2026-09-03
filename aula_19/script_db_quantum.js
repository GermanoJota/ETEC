const DATABASE_URL = "postgresql://neondb_owner:npg_C6ysFZK7TMHn@ep-little-poetry-ackjvh1e-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"    //  colocar a URL de conexão
const host = new URL(DATABASE_URL).host
const neonHttpEndPoint = `https://${host}/sql`

// console.log(DATABASE_URL, host, neonHttpEndPoint);

async function executarQueryNeon(querySQL,parametros=[]) {
    try {
        const resposta = await fetch(neonHttpEndPoint,
            {
                method:'POST',
                headers:{
                    'Neon-Connection-String':DATABASE_URL,
                    'Content-Type':'Application/json'
                },
                body:JSON.stringify({
                    query:querySQL,
                    params:parametros
                })
            });
            
            if(!resposta.ok)
            {
                const erroTexto = await resposta.text();
                throw new error(`Erro HTTP ${resposta.status}: ${erroTexto}`)
            }
            const dados = await resposta.json();
            return dados.rows;
    }
    catch (error) {
        console.error("Falha ao comunicar com o banco de dados", error)
        return null
    }

}
    const categoriaMock = [
        {categoria:'Eletronicos'},
        {categoria:'Biblioteca'},
        {categoria:'Moveis'},
        {categoria:'Roupas'},
    ]

    async function insertData(table,coluna,data) {
        const query = `INSERT INTO ${table} (${coluna}) VALUES ($1) RETURNING *`
        const params = [data]

        const linhas = await executarQueryNeon(query, params);
        return linhas !== null;
    }

    async function testeInsert() {
        categoriaMock.forEach(element => {
            insertData("categoria", "descricao",element.categoria)
        });
    }
