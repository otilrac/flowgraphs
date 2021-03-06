#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Nogui Perf Spectrum Analyzer
# Generated: Thu Apr 18 16:23:13 2019
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class nogui_perf_spectrum_analyzer(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Nogui Perf Spectrum Analyzer")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(915000000, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(915000000, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.uhd_usrp_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=nogui_perf_spectrum_analyzer, options=None):

    tb = top_block_cls()
    tb.start(1000)
    tb.wait()
    int nitems_read = tb.nitems_read()
    print("#items read", nitems_read)

if __name__ == '__main__':
    main()
