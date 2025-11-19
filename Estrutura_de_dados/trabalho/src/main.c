/* ================== modulo: tipos/item ================== */
#include <stdio.h>
#include <string.h>

#define MAX 20

typedef enum { T_COMIDA = 0, T_BEBIDA = 1 } ItemTipo;

typedef struct {
    int id;
    char nome[16];
    float preco;
    ItemTipo tipo;
    union {
        int   kcal;            /* quando COMIDA   */
        float teor_alcoolico;  /* quando BEBIDA   */
    } extra;
} Item;

/* "construtores" simples (ajudam na prova) */
Item novo_comida(int id, const char *nome, float preco, int kcal) {
    Item it;
    it.id = id; it.preco = preco; it.tipo = T_COMIDA;
    strncpy(it.nome, nome, sizeof(it.nome)-1);
    it.nome[sizeof(it.nome)-1] = '\0';
    it.extra.kcal = kcal;
    return it;
}
Item novo_bebida(int id, const char *nome, float preco, float abv) {
    Item it;
    it.id = id; it.preco = preco; it.tipo = T_BEBIDA;
    strncpy(it.nome, nome, sizeof(it.nome)-1);
    it.nome[sizeof(it.nome)-1] = '\0';
    it.extra.teor_alcoolico = abv;
    return it;
}

/* impressao de um item (somente leitura com ponteiro const) */
void imprimir_item(const Item *p) {
    if (!p) return;
    if (p->tipo == T_COMIDA)
        printf("[#%d] %s | R$ %.2f | COMIDA | %d kcal\n",
               p->id, p->nome, p->preco, p->extra.kcal);
    else
        printf("[#%d] %s | R$ %.2f | BEBIDA | %.1f%% ABV\n",
               p->id, p->nome, p->preco, p->extra.teor_alcoolico);
}

/* ================== modulo: lista (vetor homogeneo) ================== */
/* Inserir no fim usando ponteiro para n (tamanho usado) */
int inserir(Item vet[], int *n, Item x) {
    if (*n >= MAX) return 0;      /* falha: cheio */
    vet[*n] = x;
    (*n)++;
    return 1;                      /* sucesso */
}

/* Buscar por id: retorna ponteiro para o elemento ou NULL */
Item* buscar(Item vet[], int n, int id) {
    for (int i = 0; i < n; i++)
        if (vet[i].id == id) return &vet[i];
    return NULL;
}

/* Listar todos (somente leitura) */
void listar(const Item vet[], int n) {
    for (int i = 0; i < n; i++)
        imprimir_item(&vet[i]);
}

/* ================== modulo: app (main de demonstracao) ================== */
int main(void) {
    Item vet[MAX];
    int n = 0;

    /* insercoes de exemplo (sem entrada do usuario para caber no papel) */
    inserir(vet, &n, novo_comida(1, "Sopa",   15.0f, 250));
    inserir(vet, &n, novo_bebida(2, "Cerva",  12.0f, 5.0f));
    inserir(vet, &n, novo_comida(3, "Pao",     5.0f, 120));

    puts("== Lista ==");
    listar(vet, n);

    puts("\n== Busca id=2 ==");
    Item *p = buscar(vet, n, 2);
    if (p) imprimir_item(p); else puts("Nao encontrado.");

    return 0;
}
