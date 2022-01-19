### Write once, run everywhere

**Año 1991**: Creado por Sun MicroSystem (James Gosling y Patrick Naughton)
**Case Sensitive**: Distingue Minúscula de mayúscula 
## Convención de nombres

- **CamelCase**: Ej: nombreCompleto
- **snake_case**: Ej: nombre_completo
- **SCREAMING_SNAKE_CASE**: NOMBRE_COMPLETO
- **kebab-case**: nombre-completo

## Operar números dentro de una cadena


Ejemplo: 

```java
public class Main {
    
    public static void main(String[] args){
        String name = "Marco";
        int edad = 31;
        int anoNacimiento = 1990;
        System.out.println("Soy "+name+" y tengo "+(edad+anoNacimiento)+ " años");        
    }
}

```


<p align="center">
<iframe
  src="https://carbon.now.sh/embed?bg=rgba%28205%2C223%2C239%2C1%29&t=blackboard&wt=sharp&l=text%2Fx-java&ds=true&dsyoff=21px&dsblur=68px&wc=true&wa=true&pv=13px&ph=15px&ln=true&fl=1&fm=Hack&fs=14px&lh=229%25&si=false&es=2x&wm=false&code=package%2520example%253B%250A%250Apublic%2520class%2520ExampleVariable%2520%257B%250A%2520%2520public%2520static%2520void%2520main%28String%255B%255D%2520args%29%257B%250A%2520%2520%2520%2520String%2520name%2520%253D%2520%2522Marco%2522%253B%250A%2520%2520%2520%2520int%2520age%2520%253D%252031%253B%250A%2520%2520%2520%2520System.out.println%28%2522I%27m%2520%2522%252Bname%252B%2522%2520and%2520have%2520%2522%252B%28age%29%252B%2522%2520old%2522%29%253B%250A%2520%2520%257D%250A%257D"
  style="width: 620px; height: 388px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>
</p>