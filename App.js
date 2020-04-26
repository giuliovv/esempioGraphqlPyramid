import React from "react";
import ApolloClient from 'apollo-boost';
import { gql } from "apollo-boost";
import { ApolloProvider, useQuery } from "@apollo/react-hooks";

//Graphql

const client = new ApolloClient({
    uri: '/graph',
  });

  const CIAO = gql`
query Ciao($nome: String){
        ciao(nome: $nome){
            esempio
        }
      }
    `;
  
    // Questo non l'ho chiamato ma in caso è come con l'altro
  const BUONGIORNO = gql`
  query Buongiorno($nome: String){
      buongiorno
  }
      `;

function Contenuto(props){
    // Qua fai robe tipo rifare una richiesta cambiando il nome pro
    props.resQuery.refetch({ nome : "Ugo" })
    // O chiamare semplicemente il contenuto
    console.log(props.resQuery.data.ciao[0].esempio) // Dovrebbe stampare ciao Ugo
}

function FaQuery() {
    // Qua chiama la query e passa quello che sta succedendo e quando è tutto pronto anche i valori
    const { loading, error, data, refetch } = useQuery(CIAO, { errorPolicy: 'all' });
    var resQuery = {"loading":loading, "error": error, "data": data, "refetch": refetch};

    return <Contenuto resQuery={resQuery}/>
}

function App() {
    return (<ApolloProvider client={client}><FaQuery /></ApolloProvider>);
}

render(<App />, document.getElementById("root"));

export default App