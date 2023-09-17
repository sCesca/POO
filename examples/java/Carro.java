// carro é uma subclasse de veiculo
public class Carro extends Veiculo
{
    private int cilindradas;
    private boolean airbag;

    Carro(int ano, String modelo, String marca, int cilindradas)
    {
        super(ano, modelo, marca);

        this.cilindradas = cilindradas;
    }

    public String toString()
    {
        return "Carro fabricado em " + getAnoDeFabricacao() + " com " + cilindradas + " cilindradas"
    }

    public static void main(String args[])
    {
        Carro = new Carro(2010, "Palio", "Fiat", 2890);

        System.out.println("O veiculo criado foi " + Carro);
    }
}