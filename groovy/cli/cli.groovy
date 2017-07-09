#!/usr/bin/env groovy
// #!/usr/bin/env groovy -cp ${HOME}/bin

def cli = new CliBuilder(usage: 'cli.groovy')
cli.'h'(longOpt: 'help', 'usage information')
cli.a('display a')
cli.b('display b', required: true) // required: false
cli.c('display c', args: 1, argName:'file')
cli.d('display d', args: 2, argName:'key=value', valueSeparator:'=')


def opt = cli.parse(args)

println "opt a ${opt.a}"
println "opt b ${opt.b}"
println "opt c ${opt.c}"
println "opt d ${opt.d}"
println "opt ds ${opt.ds}"
println "opt h ${opt.h}"


if (!opt)
    System.exit(2)

if (opt.'h') {
    cli.usage()
    return
}

