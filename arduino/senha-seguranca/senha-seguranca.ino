// C++ code
// Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto

#include <Keypad.h>

// Declaração de constantes da quantidade de linhas e colunas do teclado

const byte linhaTeclado = 4;
const byte colunaTeclado = 4;
const int ledVermelho = 12;
const int ledVerde = 11;

// Declaração de variáveis comuns

String senha = "1234";
String senhaDigitada = "";
char teclaPressionada;

// Declaração de cada tecla do teclado

char tecladoDeMembrana[linhaTeclado][colunaTeclado] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

// Declaração de conexões de pinos das linhas e colunas do teclado

byte pinoLinha[linhaTeclado] = {
  9,8,7,6
};

byte pinoColuna[colunaTeclado] = {
  5,4,3,2
};

// Declaração de Objetos Kaypad: Criando a inicialização do teclado matricial

Keypad layoutTeclado = Keypad(makeKeymap(tecladoDeMembrana), pinoLinha, pinoColuna, linhaTeclado, colunaTeclado);

void setup()
{
  Serial.begin(9600);

  // Declarando os LEDs como saída

  pinMode(ledVermelho, OUTPUT);
  pinMode(ledVerde, OUTPUT);

  // Declarando o desligamento dos LEDs

  digitalWrite(ledVermelho, LOW);
  digitalWrite(ledVerde, LOW);
}

void loop() 
{
  teclaPressionada = layoutTeclado.getKey(); // Permiti coletar a tecla digitada

  if (teclaPressionada) 
  {  
    senhaDigitada += teclaPressionada;

    if (teclaPressionada == 'C'){
      senhaDigitada = "";
      Serial.println(senhaDigitada);
      Serial.println("Pode inserir a senha novamente!");
      Serial.println(senhaDigitada);
    }  

    if (teclaPressionada == '#') 
    {
      // Removendo o último caractere digitado
      senhaDigitada.remove(senhaDigitada.length() - 1);
      
      if (senhaDigitada == senha) {
        Serial.println("Carregando o sistema!");
        delay(1500);
        Serial.println("Analisando! Aguarde alguns instantes");
        delay(2000);
        Serial.println("Senha correta! WELCOME TO THE HOUSE");
		
       // Piscar o LED verde
       for (int a = 0; a < 5; a++) 
       {
          digitalWrite(ledVerde, HIGH);
          delay(500);
          digitalWrite(ledVerde, LOW);
          delay(500);
       }  
      } else {
        Serial.println("Carregando o sistema!");
        delay(1500);
        Serial.println("Analisando! Aguarde alguns instantes");
        delay(2000);
        Serial.println("Senha incorreta! ACESS DENIED");
	   
       // Piscar o LED vermelho
       for (int b = 0; b < 5; b++) 
       {
          digitalWrite(ledVermelho, HIGH);
          delay(500);
          digitalWrite(ledVermelho, LOW);
          delay(500);
       }  
      }    
    }
  }
}