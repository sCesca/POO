public class Veiculo 
{
    private int anoDeFabricacao;
    private String modelo;
    private String marca;

    Veiculo(int anoDeFabricacao, String modelo, String marca)
    {
        this.anoDeFabricacao = anoDeFabricacao;
        this.modelo = modelo;
        this.marca = marca;
    }

    public int anoDeFabricacao()
    {
        return anoDeFabricacao;
    }

    public void setAnoDeFrabricacao(int anoDeFabricacao)
    {
        this.anoDeFabricacao = anoDeFabricacao
    }
}