export interface ResultadoType {
  producao_media: number;
  producao_total: number;
  economia: number;
}

const Resultado = ({
  producao_media,
  producao_total,
  economia,
}: ResultadoType) => {
  return (
    <div className="text-slate-950 bg-slate-100 p-2 rounded w-96 flex flex-col gap-3">
      <h1 className="text-2xl">Resultados</h1>
      <p>Produção Média (Mensal): {Number(producao_media).toFixed(2)} kWh</p>
      <p>Produção Total (25 anos): {Number(producao_total).toFixed(2)} kWh</p>
      <p>Economia total (25 anos): R$ {Number(economia).toFixed(2)}</p>
    </div>
  );
};

export default Resultado;
