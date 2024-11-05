import { useState } from "react";
import Resultado from "./components/Resultado";
import ResultadoType from "./components/Resultado";

function App() {
  const [placas, setPlacas] = useState("");
  const [valorPlaca, setValorPlaca] = useState("");
  const [valorKwh, setValorKwh] = useState("");
  const [temperatura, setTemperatura] = useState("");
  const [result, setResult] = useState<ResultadoType | null>(null);

  const handleClick = async (
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
    e.preventDefault();

    const url = "http://localhost:8001/solar/";
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          numero_placas: placas,
          valor_placa: valorPlaca,
          valor_energia: valorKwh,
          temperatura: temperatura,
        }),
      });

      if (!response.ok) {
        throw new Error(`Erro: ${response.statusText}`);
      }

      const data = await response.json();
      // Supondo que `data` contenha `producao_media` e `producao_total`
      const resultado: ResultadoType = {
        producao_media: data.producao_media,
        producao_total: data.producao_total,
        economia: data.economia,
      };
      setResult(resultado);
      console.log(data); // Exibe a resposta JSON no console
    } catch (error) {
      console.error("Erro ao enviar requisição:", error);
    }
  };

  return (
    <>
      <div className="w-screen h-screen bg-slate-900 flex justify-center items-center flex-col gap-8">
        <form className="w-96 flex flex-col gap-4 ">
          <h1 className="text-slate-100 text-lg">Calculo Energia Solar</h1>
          <input
            type="number"
            name="numero_placas"
            placeholder="Numero de placas, ex: 3"
            className="h-9 rounded p-1"
            onChange={(e) => setPlacas(e.target.value)}
          />
          <input
            type="number"
            name="valor_placa"
            placeholder="Valor da placa, ex: 500"
            className="h-9 rounded p-1"
            onChange={(e) => setValorPlaca(e.target.value)}
          />
          <input
            type="number"
            name="valor_kwv"
            placeholder="Valor kWh, ex: 1.2"
            className="h-9 rounded p-1"
            onChange={(e) => setValorKwh(e.target.value)}
          />
          <input
            type="number"
            name="temperatura"
            placeholder="Temperatura, ex: 25.5"
            className="h-9 rounded p-1"
            onChange={(e) => setTemperatura(e.target.value)}
          />
          <button
            className="text-slate-100 bg-slate-700 h-9 rounded"
            onClick={(e) => handleClick(e)}
          >
            Enviar
          </button>
        </form>
        {result ? (
          <Resultado
            producao_media={result.producao_media}
            producao_total={result.producao_total}
            economia={result.economia}
          />
        ) : null}
      </div>
    </>
  );
}

export default App;
