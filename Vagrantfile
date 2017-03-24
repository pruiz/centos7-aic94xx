# -*- mode: ruby -*-
# vi: set ft=ruby :

# Minimun vagrant version required for this environment.
Vagrant.require_version ">= 1.7.4"

Vagrant.configure(2) do |config|

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/centos-7.3"
  config.vm.box_version = "2.3.4"
  config.vm.hostname = "centos7-aic94xx.sandbox"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  #config.vm.synced_folder "pillars", "/srv/salt/pillars", create: true, owner: "root", group: "root"

  # Ensure we uselinked-clones under parallels.
  config.vm.provider "parallels" do |prov|
    if prov.respond_to?("linked_clone") then prov.linked_clone else prov.use_linked_clone end
  end

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  # Install/Update ca-certificates package..
  config.vm.provision "shell", inline: <<-SHELL
    yum -y --disablerepo=\* --enablerepo=base --enablerepo=updates upgrade ca-certificates
    update-ca-trust

    yum groups mark convert
    yum -y install deltarpm vim-enhanced
    yum -y groupinstall 'Development Tools'
    yum -y install bc xmlto asciidoc hmaccalc python-devel newt-devel 'perl(ExtUtils::Embed)' pesign elfutils-devel zlib-devel binutils-devel audit-libs-devel numactl-devel pciutils-devel ncurses-devel
    yum -y --enablerepo=extras install epel-release
    yum -y install dkms
  SHELL

end
