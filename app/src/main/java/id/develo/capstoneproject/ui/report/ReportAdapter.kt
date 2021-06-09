package id.develo.capstoneproject.ui.report

import android.content.Intent
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import id.develo.capstoneproject.data.local.entity.ReportEntity
import id.develo.capstoneproject.databinding.ItemReportBinding

class ReportAdapter(private val listReports: ArrayList<ReportEntity>) :
    RecyclerView.Adapter<ReportAdapter.ReportViewHolder>() {

    inner class ReportViewHolder(private val binding: ItemReportBinding) :
        RecyclerView.ViewHolder(binding.root) {
            fun bind(report: ReportEntity) {
                with(binding) {
                    tvStreet.text = "${report.latitude}, ${report.longitude}"
                    tvCategory.text = report.holeType
                    Glide.with(itemView.context)
                        .load("https://storage.googleapis.com/pothole-detection1/" + report.urlImg)
                        .into(imgUser)

                    itemView.setOnClickListener {
                        val intentDetail = Intent(itemView.context, ReportDetailActivity::class.java)
                        intentDetail.putExtra(ReportDetailActivity.EXTRA_REPORT, report)
                        itemView.context.startActivity(intentDetail)
                    }
                }
            }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ReportViewHolder {
        val binding =
            ItemReportBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ReportViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ReportViewHolder, position: Int) {
        holder.bind(listReports[position])
    }

    override fun getItemCount(): Int = listReports.size
}