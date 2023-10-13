from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import argparse


#parser = argparse.ArgumentParser()
#parser.add_argument("--file", required=True, type=str, help="Input large fasta file from Kraken.")
#parser.add_argument("--out", required=True, type=str, help="Output to individual fasta for each genome.")
#args=parser.parse_args()

class IDXCleanPlugin:
  def input(self, inputfile):
     self.INPUT_FASTA = inputfile
  def run(self):
     pass
  def output(self, outputfile):
   OUT_FASTA = outputfile

   with open(OUT_FASTA, "w") as f:
    for record in SeqIO.parse(self.INPUT_FASTA, "fasta"):
        sequence_attributes = record.description
        tax_id = sequence_attributes.split("|")[1]
        sq_name = sequence_attributes.split("|")[2].replace(" ","_").replace(",","").replace(".","_")
        updated_record = record
        updated_record.id = tax_id + "_" + sq_name
        updated_record.description=""
        SeqIO.write(updated_record, f, "fasta")
